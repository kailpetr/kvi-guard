from runtime.verifier import verify_response


response = "The atmosphere scatters blue light because of Rayleigh scattering."


result = verify_response(response)


print("State:", result["state"])
print("Score:", result["score"])
print("Telemetry:", result["telemetry"])
