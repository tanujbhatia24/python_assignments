import psutil

# Creating the function
def monitor_cpu_usage():
    print("Monitoring CPU usage...")

    # Setting infinite loop for continuous monitoring
    while(True):

        try:
            # CPU usage percentage storing in the variable named cpu_usage having interval value set to 1
            cpu_usage = psutil.cpu_percent(interval=1)

            # Checking if the CPU usage exceeds the threshold
            if cpu_usage > 80:
                print("Alert! CPU usage exceeds threshold: ",cpu_usage,"%")
            else:
                print("Current CPU usage: ",cpu_usage,"%")

        # Exception handling when stop by user
        except KeyboardInterrupt:
                print("\nMonitoring stopped by user.")
                break
        
        # Exception handling if any error triggeres
        except Exception as e:
                print(f"An error occurred: {e}")
                break

# Creating main logic, so that function/code should be available for import and reuse in other programs.    
if __name__ == "__main__":
     try:
         monitor_cpu_usage()
     except Exception as e:
        print(f"An error occurred in the main program: {e}")