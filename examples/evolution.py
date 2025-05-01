from ncviewer import NcView


ncv = NcView("examples/ncfiles/advection/IC-heaviside/advection-lax_friedichs.nc")


print(ncv.data)

ncv.evolution(0)