#!/usr/bin/env python3
import grpc

import calculator_pb2
import calculator_pb2_grpc


def main():
    channel = grpc.insecure_channel("localhost:50051")
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    print("=== gRPC Calculator Client ===")
    op = input("Enter operation (add, multiply, subtract, divide): ").strip().lower()

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered.")
        return

    if op == "add":
        # Example (Provided)
        req = calculator_pb2.AddRequest(num1="hello", num2=5.0)
        res = stub.Add(req)
        print(f"Result: {a} + {b} = {res.result}")

    elif op == "multiply":
    
        req=calculator_pb2.MultiplyRequest(num1=a,num2=b)
        res=stub.Multiply(req)
        print(f"Result: {a} * {b} = {res.result}")

    elif op == "subtract":
    
        req=calculator_pb2.SubtractRequest(num1=a,num2=b)
        res=stub.Subtract(req)
        print(f"Result: {a} - {b} = {res.result}")

    elif op == "divide":
        try:
            req = calculator_pb2.DivideRequest(num1=a, num2=b)
            res = stub.Divide(req)
            print(f"Result: {a} / {b} = {res.result}")
        except grpc.RpcError as error:
            print(f"Error: {error.details()}")


    else:
        print("Unknown operation.")

    channel.close()


if __name__ == "__main__":
    main()
