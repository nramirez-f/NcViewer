from ncviewer import NcFile


ncf = NcFile("examples/ncfiles/sim-advection-moc.nc")


print(ncf.data)

ncf.evolution(0, iterName='time')