import sys
import os
from concurrent import futures
import grpc
from proto import visual_pb2
from proto import visual_pb2_grpc
from visual import Visual

class VisualServiceServicer(visual_pb2_grpc.VisualServiceServicer):
    def __init__(self):
        # Dictionary to hold dataset paths
        self.dataset_paths = {
            'bca': './dataset/bca.csv',
            'tkm': './dataset/tkm.csv'
        }

    def _load_visual(self, dataset_name):
        # Load the dataset based on user's choice
        dataset_path = self.dataset_paths.get(dataset_name)
        if not dataset_path or not os.path.exists(dataset_path):
            raise ValueError(f"Dataset '{dataset_name}' not found.")
        
        # Create a new instance of Visual with the chosen dataset
        return Visual(dataset_path)

    def GenerateTimeSeries(self, request, context):
        # Load the Visual class with the appropriate dataset
        visual = self._load_visual(request.dataset)
        
        # Generate the time series image
        stock_data = visual.time_series(mv=request.mv, date_range=request.date_range)
        
        # Return the image data in the gRPC response
        return visual_pb2.JsonResponse(json_data=stock_data)

    def GenerateVolumeAnalysis(self, request, context):
        # Load the Visual class with the appropriate dataset
        visual = self._load_visual(request.dataset)
        
        # Generate the volume analysis image
        volume_data = visual.volume_analysis(date_range=request.date_range)
        return visual_pb2.JsonResponse(json_data=volume_data)

    def GenerateMonthlyAverage(self, request, context):
        # Load the Visual class with the appropriate dataset
        visual = self._load_visual(request.dataset)
        
        # Generate the monthly average image
        visual.monthly_average()

        # Read the saved image file as binary
        with open('./assets/table_change.png', 'rb') as image_file:
            image_data = image_file.read()

        # Return the image data in the gRPC response
        return visual_pb2.ImageResponse(image_data=image_data)

    def GeneratePriceAndPercent(self, request, context):
        # Load the Visual class with the appropriate dataset
        visual = self._load_visual(request.dataset)
        
        # Generate the price and percent change image
        price_percent_data = visual.price_and_percent(date_range=request.date_range)
        return visual_pb2.JsonResponse(json_data=price_percent_data)


# Define the gRPC server setup
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    visual_pb2_grpc.add_VisualServiceServicer_to_server(VisualServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    # Ensure the current working directory is set to the project's root
    sys.path.append(os.path.join(os.path.dirname(__file__), '../proto'))
    serve()
