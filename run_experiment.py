#! /usr/bin/python
import os

if __name__ == "__main__":

	CAMP_PED_SCRIPT_R2= "scripts/camp-ped-r2"
	CAMP_PED_SCRIPT_R4= "scripts/camp-ped-r4"
	CAMP_PED_SCRIPT_R6= "scripts/camp-ped-r6"
	CITY_DRIVE_SCRIPT_R2 = "scripts/city-drive-r2"
	CITY_DRIVE_SCRIPT_R4 = "scripts/city-drive-r4"
	CITY_DRIVE_SCRIPT_R6 = "scripts/city-drive-r6"
	HIGHWAY_DRIVE_SCRIPT_R2 = "scripts/highway-drive-r2"
	HIGHWAY_DRIVE_SCRIPT_R4 = "scripts/highway-drive-r4"
	HIGHWAY_DRIVE_SCRIPT_R6 = "scripts/highway-drive-r6"

	print("Start .........................................")
	os.system("mkdir logs")
	os.system("mkdir results")

	############################

	os.system(CAMP_PED_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/camp_ped_log_r2 > ./results/camp-ped-throughput-r2.tml")
	os.system("mm-delay-graph ./logs/camp_ped_log_r2 > ./results/camp-ped-delay-r2.html")

	os.system(CAMP_PED_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/camp_ped_log_r4 > ./results/camp-ped-throughput-r4.tml")
	os.system("mm-delay-graph ./logs/camp_ped_log_r4 > ./results/camp-ped-delay-r4.html")

	os.system(CAMP_PED_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/camp_ped_log_r6 > ./results/camp-ped-throughput-r6.tml")
	os.system("mm-delay-graph ./logs/camp_ped_log_r6 > ./results/camp-ped-delay-r6.html")
	print("Finished running camp-ped!")

	############################

	os.system(CITY_DRIVE_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/city_drive_log_r2 > ./results/city-drive-throughput-r2.tml")
	os.system("mm-delay-graph ./logs/city_drive_log_r2 > ./results/city-drive-delay-r2.html")

	os.system(CITY_DRIVE_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/city_drive_log_r4 > ./results/city-drive-throughput-r4.tml")
	os.system("mm-delay-graph ./logs/city_drive_log_r4 > ./results/city-drive-delay-r4.html")

	os.system(CITY_DRIVE_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/city_drive_log_r6 > ./results/city-drive-throughput-r6.tml")
	os.system("mm-delay-graph ./logs/city_drive_log_r6 > ./results/city-drive-delay-r6.html")
	print("Finished running the city-drive!")

	############################

	os.system(HIGHWAY_DRIVE_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/highway_drive_log_r2 > ./results/highway-drive-throughput-r2.tml")
	os.system("mm-delay-graph ./logs/highway_drive_log_r2 > ./results/highway-drive-delay-r2.html")

	os.system(HIGHWAY_DRIVE_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/highway_drive_log_r4 > ./results/highway-drive-throughput-r4.tml")
	os.system("mm-delay-graph ./logs/highway_drive_log_r4 > ./results/highway-drive-delay-r4.html")

	os.system(HIGHWAY_DRIVE_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph-verus 500 ./logs/highway_drive_log_r6 > ./results/highway-drive-throughput-r6.tml")
	os.system("mm-delay-graph ./logs/highway_drive_log_r6 > ./results/highway-drive-delay-r6.html")
	print("Finished running the highway-drive!")

	print("Finished! Look in the results directory to find the html files to download and view.")
