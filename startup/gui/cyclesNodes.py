import Gaffer
import GafferUI
import GafferScene
import GafferOSL
import GafferArnold
import GafferCycles
import GafferImage
import os
import imath


Gaffer.Metadata.registerValue( GafferCycles.CyclesShader, "icon", "/home/heri/gaffer/images/blender.png" )
Gaffer.Metadata.registerValue( GafferCycles.CyclesLight, "icon", "/home/heri/gaffer/images/blender.png" )
Gaffer.Metadata.registerValue( GafferCycles.CyclesOptions, "icon", "/home/heri/gaffer/images/blender.png" )
Gaffer.Metadata.registerValue( GafferCycles.CyclesAttributes, "icon", "/home/heri/gaffer/images/blender.png" )
Gaffer.Metadata.registerValue( GafferCycles.CyclesRender, "icon", "/home/heri/gaffer/images/blender.png" )
Gaffer.Metadata.registerValue( GafferCycles.InteractiveCyclesRender, "icon", "/home/heri/gaffer/images/blender.png" )
Gaffer.Metadata.registerValue( GafferCycles.CyclesBackground, "icon", "/home/heri/gaffer/images/blender.png" )
Gaffer.Metadata.registerValue( GafferCycles.CyclesMeshLight, "icon", "/home/heri/gaffer/images/blender.png" )


Gaffer.Metadata.registerValue(
    GafferCycles.CyclesShader,
    "nodeGadget:color", imath.Color3f( 0.25, 0.25, 0.25 )
)

Gaffer.Metadata.registerValue(
    GafferCycles.CyclesLight,
    "nodeGadget:color", imath.Color3f( 0.65, 0.55, 0.25 )
)
Gaffer.Metadata.registerValue(
    GafferCycles.CyclesOptions,
    "nodeGadget:color", imath.Color3f( 0.25, 0.25, 0.25 )
)
Gaffer.Metadata.registerValue(
    GafferCycles.CyclesAttributes,
    "nodeGadget:color", imath.Color3f( 0.25, 0.25, 0.25 )
)
Gaffer.Metadata.registerValue(
    GafferCycles.CyclesRender,
    "nodeGadget:color", imath.Color3f( 0.25, 0.25, 0.25 )
)
Gaffer.Metadata.registerValue(
    GafferCycles.InteractiveCyclesRender,
    "nodeGadget:color", imath.Color3f( 0.25, 0.25, 0.25 )
)
Gaffer.Metadata.registerValue(
    GafferCycles.CyclesBackground,
    "nodeGadget:color", imath.Color3f( 0.25, 0.25, 0.25 )
)

