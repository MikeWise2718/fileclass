# Readme

Setting up custom-tb-obs to merge easily with master branch of `Unity/ML-Agents`

1. Clone `Unity/ML-Agents` project and t
2. Load the Unity project and test the `FoodCollector` example
3. Check that Tensorflor works
4. Check that TensorBoard is working "
5. New branch (custom-to-obs) off of the master branch
6. Copy the needed files over using this `copyfile.py`
    - Use `copyfile --sdir . --ddir mlagents/ml-agents --exec
7. Install the protobuf tools
    - See the README.md in the `protobuf-definitions` subdir
    - Make sure nuget is installed and in the path
    - Intsall protobuf 
        - `pip install protobuf==3.6.0 --force`
        - `pip install grpcio-tools==1.11.1`
        - `pip install mypy-protobuf`
    - Install GRPC tools
       - `nuget install Grpc.Tools -Version 1.14.1 -OutputDirectory $MLAGENTS_ROOT\protobuf-definitions`
       - or ``nuget install Grpc.Tools -Version 1.14.1 -OutputDirectory .`
    - `make_for_win.bat` 
       - modify and  sure %COMPILER% points to the output directory above
       - `set COMPILER=D:\Unity\ml-agents\protobuf-definitions\Grpc.Tools.1.14.1\tools\windows_x64` 
      
8. Compile the protobuf things
    - If you set things up right you just have to run make_for_win.bat and see that there are no errors
    - If everything worked right 
9. Load the Unity Project and Test the FoodCollector example
10. See if TensorBoard is working


