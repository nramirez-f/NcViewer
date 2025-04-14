import os
import xarray as xr
import plotly.graph_objects as go

class NcFile:

    def __init__(self, ncf_path):
        """
        Load NetCDF file from given path
        """
        full_path = os.path.abspath(ncf_path)

        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File {full_path} not found.")
        
        try:
            self.data = xr.open_dataset(full_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load NetCDF file: {e}")
        
        print(f"Loaded: {full_path}")

    ## 1D ##
    def point(self, dimPos: int, iterPos: int, varName: str = 'u',dimName: str = 'x', iterName: str = 't'):
        """
        Plot the value of varName in dimPos of dimName at iterVal of iterName
        """
        x_data = self.data[dimName].isel({dimName: dimPos}).values
        y_data = self.data[varName].isel({dimName: dimPos, iterName: iterPos}).values

        fig = go.Figure(
            data=go.Scatter(
                x=x_data,
                y=y_data,
                mode='markers',
            )
        )

        fig.show()

    def scatter(self,  iterPos: int, varName: str = 'u', dimName: str = 'x', iterName: str = 't'):
        """
        Creates a Scatter plot for the given varName at iterPos.
        """
        x_data = self.data[dimName].values
        y_data = self.data[varName].isel({iterName: iterPos}).values

        scatter = go.Scatter(
            x=x_data,
            y=y_data,
            mode="lines"
        )

        return scatter

    def frame(self,  iterPos: int, varName: str = 'u', dimName: str = 'x', iterName: str = 't'):
        """
        Frame of varName at iterPos
        """
        fig = go.Figure(self.scatter(iterPos, varName, dimName, iterName))

        fig.show()

    def evolution(self, iterPosInit: int, varName: str = 'u', dimName: str = 'x', iterName: str = 't', delay: int = 100):
        """
        Evolution plot from iterInit to the end of iterDomain.
        """
        iterDomain = self.data[iterName].values.tolist()[iterPosInit:]

        fig = go.Figure(data=[self.scatter(iterPosInit, varName=varName, dimName=dimName, iterName=iterName)])

        frames = [
            go.Frame(
                data=[self.scatter((iterPosInit + iterPosRel), varName, dimName, iterName)],
                name=str(iterValue)
            )
            for iterPosRel, iterValue in enumerate(iterDomain)
        ]

        fig.update(frames=frames)

        eps_y = 0.1
        fig.update_layout(
            yaxis=dict(
                range=[self.data[varName].min().values - eps_y, self.data[varName].max().values + eps_y],
                title=dict(text=varName),
            ),
            xaxis=dict(
                range=[self.data[dimName].values[0], self.data[dimName].values[-1]],
                title=dict(text=dimName),
            )
        )

        fig.update_layout(
            updatemenus=[{
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": delay, "redraw": True}, "fromcurrent": True}],
                        "label": "▶ Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "❚❚ Pause",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0.1,
                "yanchor": "top"
            }]
        )

        fig.update_layout(
            sliders=[{
                "steps": [
                    {
                        "args": [[str(iterValue)], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}],
                        "label": str(iterValue),
                        "method": "animate"
                    }
                    for iterValue in iterDomain
                ],
                "x": 0.1,
                "len": 0.9,
                "xanchor": "left",
                "y": 0,
                "yanchor": "top"
            }]
        )

        fig.show()

