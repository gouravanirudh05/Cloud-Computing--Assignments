# In-Class Assignment: gRPC Basics

## Submission
Submit your `server.py` and the answers to the write-down questions on LMS.

## Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Inspect `calculator.proto`, `server.py`, and `client.py` to see the provided `Add` example.

3. Complete Task 1 in `calculator.proto`:
   Add `rpc Multiply`, `rpc Subtract`, and `rpc Divide` service definitions and messages.

4. Compile `calculator.proto`:
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

5. Complete Task 2 in `server.py`:
   Implement `Multiply`, `Subtract`, and `Divide` server methods.

6. Complete Task 3 in `client.py`:
   Implement client calls for `multiply`, `subtract`, and `divide`.

7. Run and Test:
```bash
# Terminal 1
python server.py

# Terminal 2
python client.py
```

## Write-Down Questions (Submit Answers on LMS)

1. Open `calculator_pb2_grpc.py`:
   - What is the class name of the client stub?
   - What base class does `CalculatorServicer` in `server.py` inherit from?

2. What exact steps (commands and code edits) are required to add a new `Power` RPC method before `client.py` can call it?

3. Temporarily change `client.py` to pass `"hello"` into `AddRequest(num1="hello", num2=5.0)` and run `python client.py`. What exact Python exception and error message are printed in the terminal?
