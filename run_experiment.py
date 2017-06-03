#! /usr/bin/python
import os

if __name__ == "__main__":

	CAMP_PED_SCRIPT_R2= "scripts/camp-ped-r2"
	CAMP_PED_SCRIPT_R4= "scripts/camp-ped-r4"
	CAMP_PED_SCRIPT_R6= "scripts/camp-ped-r6"
	CAMP_PED_SCRIPT_CUBIC= "scripts/camp-ped-cubic"

	CITY_DRIVE_SCRIPT_R2 = "scripts/city-drive-r2"
	CITY_DRIVE_SCRIPT_R4 = "scripts/city-drive-r4"
	CITY_DRIVE_SCRIPT_R6 = "scripts/city-drive-r6"
	CITY_DRIVE_SCRIPT_CUBIC = "scripts/city-drive-cubic"

	HIGHWAY_DRIVE_SCRIPT_R2 = "scripts/highway-drive-r2"
	HIGHWAY_DRIVE_SCRIPT_R4 = "scripts/highway-drive-r4"
	HIGHWAY_DRIVE_SCRIPT_R6 = "scripts/highway-drive-r6"
	HIGHWAY_DRIVE_SCRIPT_CUBIC = "scripts/highway-drive-cubic"

	ATT_DRIVE_SCRIPT_R2 = "scripts/att-drive-r2"
	ATT_DRIVE_SCRIPT_R4 = "scripts/att-drive-r4"
	ATT_DRIVE_SCRIPT_R6 = "scripts/att-drive-r6"
	ATT_DRIVE_SCRIPT_CUBIC = "scripts/att-drive-cubic"

	EVDO_DRIVE_SCRIPT_R2 = "scripts/evdo-drive-r2"
	EVDO_DRIVE_SCRIPT_R4 = "scripts/evdo-drive-r4"
	EVDO_DRIVE_SCRIPT_R6 = "scripts/evdo-drive-r6"
	EVDO_DRIVE_SCRIPT_CUBIC = "scripts/evdo-drive-cubic"

	TMOBILE_DRIVE_SCRIPT_R2 = "scripts/tmobile-drive-r2"
	TMOBILE_DRIVE_SCRIPT_R4 = "scripts/tmobile-drive-r4"
	TMOBILE_DRIVE_SCRIPT_R6 = "scripts/tmobile-drive-r6"
	TMOBILE_DRIVE_SCRIPT_CUBIC = "scripts/tmobile-drive-cubic"

	TEST = "scripts/test"

	print("Start .........................................")
	os.system("mkdir logs")
	os.system("mkdir results")


	############################


	os.system(CAMP_PED_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/camp_ped_log_r2 CAMP_PED_SCRIPT_R2 > ./results/camp-ped-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/camp_ped_log_r2 > ./results/camp-ped-delay-r2.html")

	os.system(CAMP_PED_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/camp_ped_log_r4 CAMP_PED_SCRIPT_R4 > ./results/camp-ped-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/camp_ped_log_r4 > ./results/camp-ped-delay-r4.html")

	os.system(CAMP_PED_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/camp_ped_log_r6 CAMP_PED_SCRIPT_R6 > ./results/camp-ped-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/camp_ped_log_r6 > ./results/camp-ped-delay-r6.html")

	os.system(CAMP_PED_SCRIPT_CUBIC)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/camp_ped_log_cubic CAMP_PED_SCRIPT_CUBIC > ./results/camp-ped-throughput-cubic.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/camp_ped_log_cubic > ./results/camp-ped-delay-cubic.html")

	print("Finished running camp-ped!")

	# ############################

	os.system(CITY_DRIVE_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/city_drive_log_r2 CITY_DRIVE_SCRIPT_R2 > ./results/city-drive-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/city_drive_log_r2 > ./results/city-drive-delay-r2.html")

	os.system(CITY_DRIVE_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/city_drive_log_r4 CITY_DRIVE_SCRIPT_R4 > ./results/city-drive-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/city_drive_log_r4 > ./results/city-drive-delay-r4.html")

	os.system(CITY_DRIVE_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/city_drive_log_r6 CITY_DRIVE_SCRIPT_R6 > ./results/city-drive-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/city_drive_log_r6 > ./results/city-drive-delay-r6.html")

	os.system(CITY_DRIVE_SCRIPT_CUBIC)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/city_drive_log_cubic CITY_DRIVE_SCRIPT_CUBIC > ./results/city-drive-throughput-cubic.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/city_drive_log_cubic > ./results/city-drive-delay-cubic.html")

	print("Finished running the city-drive!")

	
	# ############################

	os.system(HIGHWAY_DRIVE_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/highway_drive_log_r2 HIGHWAY_DRIVE_SCRIPT_R2 > ./results/highway-drive-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/highway_drive_log_r2 > ./results/highway-drive-delay-r2.html")

	os.system(HIGHWAY_DRIVE_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/highway_drive_log_r4 HIGHWAY_DRIVE_SCRIPT_R4 > ./results/highway-drive-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/highway_drive_log_r4 > ./results/highway-drive-delay-r4.html")

	os.system(HIGHWAY_DRIVE_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/highway_drive_log_r6 HIGHWAY_DRIVE_SCRIPT_R6 > ./results/highway-drive-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/highway_drive_log_r6 > ./results/highway-drive-delay-r6.html")

	os.system(HIGHWAY_DRIVE_SCRIPT_CUBIC)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/highway_drive_log_cubic HIGHWAY_DRIVE_SCRIPT_CUBIC > ./results/highway-drive-throughput-cubic.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/highway_drive_log_cubic > ./results/highway-drive-delay-cubic.html")

	print("Finished running the highway-drive!")

	############################

	os.system(ATT_DRIVE_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/att_drive_r2 ATT_DRIVE_SCRIPT_R2 > ./results/att-drive-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/att_drive_r2 > ./results/att-drive-delay-r2.html")

	os.system(ATT_DRIVE_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/att_drive_r4 ATT_DRIVE_SCRIPT_R4 > ./results/att-drive-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/att_drive_r4 > ./results/att-drive-delay-r4.html")

	os.system(ATT_DRIVE_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/att_drive_r6 ATT_DRIVE_SCRIPT_R6 > ./results/att-drive-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/att_drive_r6 > ./results/att-drive-delay-r6.html")

	os.system(ATT_DRIVE_SCRIPT_CUBIC)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/att_drive_cubic ATT_DRIVE_SCRIPT_CUBIC > ./results/att-drive-throughput-cubic.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/att_drive_cubic > ./results/att-drive-delay-cubic.html")

	print("Finished running the att-drive!")

	############################

	os.system(EVDO_DRIVE_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/evdo_drive_r2 EVDO_DRIVE_SCRIPT_R2 > ./results/evdo-drive-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/evdo_drive_r2 > ./results/evdo-drive-delay-r2.html")

	os.system(EVDO_DRIVE_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/evdo_drive_r4 EVDO_DRIVE_SCRIPT_R4 > ./results/evdo-drive-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/evdo_drive_r4 > ./results/evdo-drive-delay-r4.html")

	os.system(EVDO_DRIVE_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/evdo_drive_r6 EVDO_DRIVE_SCRIPT_R6 > ./results/evdo-drive-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/evdo_drive_r6 > ./results/evdo-drive-delay-r6.html")

	os.system(EVDO_DRIVE_SCRIPT_CUBIC)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/evdo_drive_cubic EVDO_DRIVE_SCRIPT_CUBIC > ./results/evdo-drive-throughput-cubic.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/evdo_drive_cubic > ./results/evdo-drive-delay-cubic.html")

	print("Finished running the evdo-drive!")

	############################

	os.system(TMOBILE_DRIVE_SCRIPT_R2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/tmobile_drive_r2 TMOBILE_DRIVE_SCRIPT_R2 > ./results/tmobile-drive-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/tmobile_drive_r2 > ./results/tmobile-drive-delay-r2.html")

	os.system(TMOBILE_DRIVE_SCRIPT_R4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/tmobile_drive_r4 TMOBILE_DRIVE_SCRIPT_R4 > ./results/tmobile-drive-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/tmobile_drive_r4 > ./results/tmobile-drive-delay-r4.html")

	os.system(TMOBILE_DRIVE_SCRIPT_R6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/tmobile_drive_r6 TMOBILE_DRIVE_SCRIPT_R6 > ./results/tmobile-drive-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/tmobile_drive_r6 > ./results/tmobile-drive-delay-r6.html")

	os.system(TMOBILE_DRIVE_SCRIPT_CUBIC)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/tmobile_drive_cubic TMOBILE_DRIVE_SCRIPT_CUBIC > ./results/tmobile-drive-throughput-cubic.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/tmobile_drive_cubic > ./results/tmobile-drive-delay-cubic.html")

	print("Finished running the tmobile-drive!")

	print("Finished! Look in the results directory to find the html files to download and view.")
