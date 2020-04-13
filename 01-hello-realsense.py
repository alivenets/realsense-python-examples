#####################################################
## librealsense tutorial #1 - Hello from realsense ##
#####################################################

# First import the library
import pyrealsense2 as rs
import traceback

pipeline = None

try:
    # Create a context object. This object owns the handles to all connected realsense devices
    pipeline = rs.pipeline()

    # Configure and start the pipeline
    pipeline.start()

    while True:
        # This call waits until a new coherent set of frames is available on a device
        # Calls to get_frame_data(...) and get_frame_timestamp(...) on a device
        # will return stable values until wait_for_frames(...) is called
        frames = pipeline.wait_for_frames()
        # Try to get a frame of a depth image
        depth = frames.get_depth_frame()

        if not depth:
            continue

        # Get the depth frame's dimensions
        width = depth.get_width()
        height = depth.get_height()

        # Query the distance from the camera to the object in the center of the image
        dist_to_center = depth.get_distance(int(width) / 2, int(height) / 2)

        # Print the distance
        print("The camera is facing an object %d meters away" % (dist_to_center))

    exit(0)
except Exception as e:
    print("Error was thrown: %s" % (e))
    traceback.print_exc()
    exit(1)
finally:
    if pipeline is not None:
        pipeline.stop()
