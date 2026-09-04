#!/usr/bin/env python3
import concurrent.futures
import grpc

import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    # Example (Provided): Add Handler
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.AddResponse(result=result)

    def Multiply(self, request, context):
        result=request.num1*request.num2
        return calculator_pb2.MultiplyResponse(result=result)

    def Subtract(self, request, context):
        result=request.num1-request.num2
        return calculator_pb2.SubtractResponse(result=result)

    def Divide(self, request, context):
        if (request.num2==0):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Cannot divide by zero")
            return calculator_pb2.DivideResponse()
        result=request.num1 / request.num2
        return calculator_pb2.DivideResponse(result=result)

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=4))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Calculator gRPC Server starting on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
