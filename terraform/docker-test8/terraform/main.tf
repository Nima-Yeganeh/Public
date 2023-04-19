provider "oci" {
  tenancy_ocid     = "<your tenancy OCID>"
  user_ocid        = "<your user OCID>"
  fingerprint      = "<your user fingerprint>"
  private_key_path = "<path to your private key file>"
  region           = "us-phoenix-1"
}

resource "oci_functions_application" "example" {
  compartment_id = "<your compartment OCID>"
  display_name   = "example-application"
}

resource "oci_functions_function" "example" {
  compartment_id   = "<your compartment OCID>"
  display_name     = "example-function"
  application_id   = oci_functions_application.example.id
  image            = "oraclelinux"
  image_digest     = "sha256:123abc"
  memory_in_mb     = 256
  timeout_in_seconds = 30
  invoke_endpoint  = true

  environment_variables = {
    "MY_VAR" = "my_value"
  }

  source_code {
    file_name      = "index.js"
    file_contents  = "${file("index.js")}"
    function_handler = "handler"
  }
}

output "function_invoke_url" {
  value = oci_functions_function.example.invoke_endpoint
}
