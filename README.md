# ai-utils
## Usage
### 2. Setup env
`source setupvars.sh`
### 3. Compile model for openvino
`python tf_to_openvino.py --saved_model_dir tf --output_dir openvino --input_shape "[1,416,608,3]"`
