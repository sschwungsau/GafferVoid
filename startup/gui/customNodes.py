import Gaffer
import GafferUI
import GafferScene
import GafferOSL
import GafferArnold
import GafferCycles
import GafferImage
import os
import imath

def __macbethTexture() :

	return Gaffer.Reference( "MacbethTexture" )

def __macbethTexturePostCreator( node, menu ) :

	node.load(
		os.path.expandvars( "$GAFFER_ROOT/resources/examples/references/macbethTexture.grf" )
	)

nodeMenu = GafferUI.NodeMenu.acquire( application )
nodeMenu.append(
	path = "/Custom/MacbethTexture",
	nodeCreator = __macbethTexture,
	postCreator = __macbethTexturePostCreator,
	searchText = "MacbethTexture"
)

Gaffer.Metadata.registerValue(
    GafferScene.ShaderAssignment,
    "nodeGadget:color", imath.Color3f( 0.3, 0.5, 0.5 )
)
Gaffer.Metadata.registerValue(
    GafferScene.Prune,
    "nodeGadget:color", imath.Color3f( 0.5, 0.1, 0.5 )
)
Gaffer.Metadata.registerValue(
    GafferScene.Isolate,
    "nodeGadget:color", imath.Color3f( 0.5, 0.1, 0.5 )
)
Gaffer.Metadata.registerValue(
    GafferScene.SceneReader,
    "nodeGadget:color", imath.Color3f( 0.0, 0.5, 0.0 )
)
Gaffer.Metadata.registerValue(
    GafferScene.ExternalProcedural,
    "nodeGadget:color", imath.Color3f( 0.0, 0.5, 0.0 )
)
Gaffer.Metadata.registerValue(
    GafferImage.ImageReader,
    "nodeGadget:color", imath.Color3f( 0.1, 0.6, 0.0 )
)

Gaffer.Metadata.registerValue(
    GafferArnold.ArnoldShader,
    "nodeGadget:color", imath.Color3f( 0.35, 0.35, 0.45 )
)
Gaffer.Metadata.registerValue(
    GafferArnold.ArnoldLight,
    "nodeGadget:color", imath.Color3f( 0.65, 0.55, 0.25 )
)



Gaffer.Metadata.registerValue( GafferImage.BleedFill, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Blur, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Catalogue, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.CatalogueSelect, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Checkerboard, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Clamp, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.CollectImages, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.ColorSpace, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Constant, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.CopyChannels, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.CopyImageMetadata, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Crop, "icon", "/home/heri/gaffer/images/images.png" )

Gaffer.Metadata.registerValue( GafferImage.DeleteChannels, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.DeleteImageMetadata, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Dilate, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Display, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.DisplayTransform, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Erode, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Grade, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.ImageNode, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.ImageProcessor, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.ImageReader, "icon", "/home/heri/gaffer/images/reader.png" )
Gaffer.Metadata.registerValue( GafferImage.ImageSampler, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.ImageStats, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.ImageTransform, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.ImageWriter, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.LUT, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Median, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Merge, "icon", "/home/heri/gaffer/images/layers.png" )
Gaffer.Metadata.registerValue( GafferImage.Mirror, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Mix, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Offset, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.OpenImageIOReader, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Premultiply, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Ramp, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Rectangle, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Resample, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Resize, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Shuffle, "icon", "/home/heri/gaffer/images/images.png" )
Gaffer.Metadata.registerValue( GafferImage.Text, "icon", "/home/heri/gaffer/images/images.png" )

Gaffer.Metadata.registerValue( GafferScene.SceneReader, "icon", "/home/heri/gaffer/images/reader.png" )
Gaffer.Metadata.registerValue( GafferScene.Instancer, "icon", "/home/heri/gaffer/images/instancer.png" )
Gaffer.Metadata.registerValue( GafferScene.Orientation, "icon", "/home/heri/gaffer/images/orient.png" )
Gaffer.Metadata.registerValue( GafferScene.Set, "icon", "/home/heri/gaffer/images/sets.png" )
Gaffer.Metadata.registerValue( GafferScene.SetVisualiser, "icon", "/home/heri/gaffer/images/sets.png" )
Gaffer.Metadata.registerValue( GafferScene.PathFilter, "icon", "/home/heri/gaffer/images/search.png" )
Gaffer.Metadata.registerValue( GafferScene.Parent, "icon", "/home/heri/gaffer/images/parent.png" )
Gaffer.Metadata.registerValue( GafferScene.Outputs, "icon", "/home/heri/gaffer/images/forward.png" )
Gaffer.Metadata.registerValue( GafferScene.StandardOptions, "icon", "/home/heri/gaffer/images/screen.png" )
Gaffer.Metadata.registerValue( GafferScene.ShaderAssignment, "icon", "/home/heri/gaffer/images/asterix.png" )
Gaffer.Metadata.registerValue( GafferScene.Camera, "icon", "/home/heri/gaffer/images/camera.png" )
Gaffer.Metadata.registerValue( GafferScene.Transform, "icon", "/home/heri/gaffer/images/move.png" )
Gaffer.Metadata.registerValue( GafferScene.DeletePoints, "icon", "/home/heri/gaffer/images/prune.png" )
Gaffer.Metadata.registerValue( GafferScene.ExternalProcedural, "icon", "/home/heri/gaffer/images/reader.png" )

Gaffer.Metadata.registerValue( Gaffer.TimeWarp, "icon", "/home/heri/gaffer/images/watch.png" )

Gaffer.Metadata.registerValue( GafferOSL.OSLShader, "icon", "/home/heri/gaffer/images/osl.png" )
Gaffer.Metadata.registerValue( GafferOSL.OSLObject, "icon", "/home/heri/gaffer/images/osl.png" )
Gaffer.Metadata.registerValue( GafferOSL.OSLImage, "icon", "/home/heri/gaffer/images/osl.png" )

Gaffer.Metadata.registerValue( GafferArnold.ArnoldShader, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldLight, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldOptions, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldAttributes, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldRender, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.InteractiveArnoldRender, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldAOVShader, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldDisplacement, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldAtmosphere, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldVDB, "icon", "/home/heri/gaffer/images/arnold.png" )
Gaffer.Metadata.registerValue( GafferArnold.ArnoldTextureBake, "icon", "/home/heri/gaffer/images/arnold.png" )


