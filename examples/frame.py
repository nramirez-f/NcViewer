from ncviewer import NcView


ncv = NcView("examples/ncfiles/advection/IC-heaviside/advection-cir.nc")


print(ncv.data)

ncv.frame(100)