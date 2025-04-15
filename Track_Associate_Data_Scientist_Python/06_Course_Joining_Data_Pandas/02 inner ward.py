import pandas as pd
wards = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\ward.p')
census = pd.read_pickle(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\06_Course_Joining_Data_Pandas\datasets\census.p')

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

# Print the first few rows of the wards_altered table to view the change 
print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on='ward')

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)

# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on='ward')

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)



#    ward                   alderman                            address    zip
# 0    61         Proco "Joe" Moreno          2058 NORTH WESTERN AVENUE  60647
# 1     2              Brian Hopkins         1400 NORTH  ASHLAND AVENUE  60622
# 2     3                 Pat Dowell            5046 SOUTH STATE STREET  60609
# 3     4           William D. Burns    435 EAST 35TH STREET, 1ST FLOOR  60616
# 4     5         Leslie A. Hairston              2325 EAST 71ST STREET  60649
# 5     6         Roderick T. Sawyer   8001 S. MARTIN LUTHER KING DRIVE  60619
# 6     7        Gregory I. Mitchell              2249 EAST 95TH STREET  60617
# 7     8         Michelle A. Harris    8539 SOUTH COTTAGE GROVE AVENUE  60619
# 8     9           Anthony A. Beale                34 EAST 112TH PLACE  60628
# 9    10      Susan Sadlowski Garza           10500 SOUTH EWING AVENUE  60617
# 10   11     Patrick Daley Thompson          3659 SOUTH HALSTED STREET  60609
# 11   12            George Cardenas           3476 SOUTH ARCHER AVENUE  60608
# 12   13                Marty Quinn            6500 SOUTH PULASKI ROAD  60629
# 13   14            Edward M. Burke              2650 WEST 51ST STREET  60632
# 14   15           Raymond A. Lopez              1650 WEST 63RD STREET  60636
# 15   16            Toni L. Foulkes              3045 WEST 63RD STREET  60629
# 16   17             David H. Moore          7313 SOUTH ASHLAND AVENUE  60636
# 17   18          Derrick G. Curtis            8359 SOUTH PULASKI ROAD  60652
# 18   19          Matthew J. O'Shea         10400 SOUTH WESTERN AVENUE  60643
# 19   20          Willie B. Cochran    6357 SOUTH COTTAGE GROVE AVENUE  60637
# 20   21    Howard B. Brookins, Jr.  9011 SOUTH ASHLAND AVENUE, UNIT B  60620
# 21   22              Ricardo Munoz        2500 SOUTH ST. LOUIS AVENUE  60623
# 22   23        Michael R. Zalewski           6247 SOUTH ARCHER AVENUE  60638
# 23   24         Michael Scott, Jr.           1158 SOUTH KEELER AVENUE  60624
# 24   25       Daniel "Danny" Solis      1800 SOUTH BLUE ISLAND AVENUE  60608
# 25   26          Roberto Maldonado          2511 WEST DIVISION STREET  60622
# 26   27        Walter Burnett, Jr.             4 NORTH WESTERN AVENUE  60612
# 27   28             Jason C. Ervin              2602 WEST 16TH STREET  60612
# 28   29           Chris Taliaferro             6272 WEST NORTH AVENUE  60639
# 29   30          Ariel E. Reyboras        3559 NORTH MILWAUKEE AVENUE  60641
# 30   31  Milagros "Milly" Santiago            2521 NORTH PULASKI ROAD  60639
# 31   32           Scott Waguespack         2657 NORTH CLYBOURN AVENUE  60614
# 32   33               Deborah Mell         3001 WEST IRVING PARK ROAD  60618
# 33   34           Carrie M. Austin              507 WEST 111TH STREET  60628
# 34   35        Carlos Ramirez-Rosa           2710 NORTH SAWYER AVENUE  60647
# 35   36           Gilbert Villegas                 6934 WEST DIVERSEY  60607
# 36   37              Emma M. Mitts           4924 WEST CHICAGO AVENUE  60651
# 37   38           Nicholas Sposato          3821  NORTH HARLEM AVENUE  60634
# 38   39           Margaret Laurino          4404 WEST LAWRENCE AVENUE  60630
# 39   40        Patrick J. O'Connor          5850 NORTH LINCOLN AVENUE  60659
# 40   41      Anthony V. Napolitano           7442 NORTH HARLEM AVENUE  60631
# 41   42             Brendan Reilly   325 WEST HURON STREET, SUITE 510  60654
# 42   43             Michelle Smith          2523 NORTH HALSTED STREET  60614
# 43   44                 Tom Tunney        3223 NORTH SHEFFIELD AVENUE  60657
# 44   45              John S. Arena        4754 NORTH MILWAUKEE AVENUE  60630
# 45   46            James Cappleman         4544 NORTH BROADWAY AVENUE  60640
# 46   47                Ameya Pawar          4243 NORTH LINCOLN AVENUE  60618
# 47   48             Harry Osterman         5533 NORTH BROADWAY AVENUE  60640
# 48   49                  Joe Moore        7356 NORTH GREENVIEW AVENUE  60626
# 49   50       Debra L. Silverstein    2949 WEST DEVON AVENUE, SUITE A  60659




#     ward  pop_2000  pop_2010 change                                            address    zip
# 0   None     52951     56149     6%                        2765 WEST SAINT MARY STREET  60647
# 1      2     54361     55805     3%                           WM WASTE MANAGEMENT 1500  60622
# 2      3     40385     53039    31%                                17 EAST 38TH STREET  60653
# 3      4     51953     54589     5%            31ST ST HARBOR BUILDING LAKEFRONT TRAIL  60653
# 4      5     55302     51455    -7%            JACKSON PARK LAGOON SOUTH CORNELL DRIVE  60637
# 5      6     54989     52341    -5%                               150 WEST 74TH STREET  60636
# 6      7     54593     51581    -6%                          8549 SOUTH OGLESBY AVENUE  60617
# 7      8     54039     51687    -4%                         1346-1352 EAST 75TH STREET  60649
# 8      9     52008     51519    -1%                 11039-11059 SOUTH WENTWORTH AVENUE  60628
# 9     10     56613     51535    -9%                               10534 SOUTH AVENUE F  46394
# 10    11     64228     51497   -20%                            943-947 WEST 14TH PLACE  60607
# 11    12     68922     52235   -24%                         CP 46 STEVENSON EXPRESSWAY  60632
# 12    13     64382     53722   -17%                    SOUTH RAMP SOUTH LARAMIE AVENUE  60638
# 13    14     80143     54031   -33%                              4540 WEST 51ST STREET  60632
# 14    15     56057     51501    -8%    CHICAGO FIRE DEPARTMENT ENGINE COMPANY 123 2215  60632
# 15    16     50205     51954     3%                             6036 SOUTH WOOD STREET  60636
# 16    17     49264     51846     5%                       7216 SOUTH WINCHESTER AVENUE  60636
# 17    18     55043     52992    -4%                          3286 WEST COLUMBUS AVENUE  60652
# 18    19     54546     51525    -6%                        9999 SOUTH FRANCISCO AVENUE  60805
# 19    20     51854     52372     1%                     DAN RYAN EXPRESSWAY PARK MANOR  60621
# 20    21     51751     51632     0%                     8852-8854 SOUTH EMERALD AVENUE  60620
# 21    22     59734     53515   -10%                              4233 WEST 36TH STREET  60632
# 22    23     63691     53728   -16%  CHICAGO MIDWAY INTERNATIONAL AIRPORT WEST 62ND...  60629
# 23    24     50879     54909     8%                       1635 SOUTH CHRISTIANA AVENUE  60623
# 24    25     55954     54539    -3%                      1632-1746 SOUTH MILLER STREET  60608
# 25    26     56841     53516    -6%             LITTLE CUBS FIELD COMFORT STATION 1400  60622
# 26    27     61287     52939   -14%                      2151-2153 WEST CHICAGO AVENUE  60651
# 27    28     49423     55199    12%                        RML SPECIALTY HOSPITAL 3435  60624
# 28    29     61949     55267   -11%                        1241 NORTH RIDGELAND AVENUE  60302
# 29    30     72698     55560   -24%                          5118 WEST FLETCHER STREET  60641
# 30    31     65045     53724   -17%                          2854 NORTH KEATING AVENUE  60641
# 31    32     57204     55184    -4%                        2901 NORTH WASHTENAW AVENUE  60618
# 32    33     63695     55598   -13%                    4041-4043 NORTH RICHMOND STREET  60625
# 33    34     49922     51599     3%                    11544-11546 SOUTH PEORIA STREET  60827
# 34    35     57588     55281    -4%                           3634 WEST BELMONT AVENUE  60618
# 35    36     63376     54766   -14%                       2918 NORTH RUTHERFORD AVENUE  60634
# 36    37     56120     51538    -8%                         4738-4748 WEST RICE STREET  60651
# 37    38     66011     56001   -15%                    7307-7331 WEST IRVING PARK ROAD  60706
# 38    39     64291     55882   -13%                  QUEEN OF ALL SAINTS BASILICA 6280  60646
# 39    40     58652     55319    -6%                         5536 NORTH ARTESIAN AVENUE  60645
# 40    41     56127     55991     0%                          1652 SOUTH CLIFTON AVENUE  60068
# 41    42     68102     55870   -18%                          410-420 WEST GRAND AVENUE  60654
# 42    43     57668     56170    -3%                              LINCOLN PARK ZOO 2001  60614
# 43    44     58758     56058    -5%                         507-513 WEST ALDINE AVENUE  60657
# 44    45     60653     55967    -8%       CONGREGATIONAL CHURCH OF JEFFERSON PARK 5320  60630
# 45    46     56587     53784    -5%                 UPTOWN BROADWAY BUILDING 4743-4763  60640
# 46    47     52108     55074     6%                           2153 WEST BERTEAU AVENUE  60618
# 47    48     56246     55014    -2%                         1025 WEST HOLLYWOOD AVENUE  60660
# 48    49     59435     54633    -8%                             1426 WEST ESTES AVENUE  60645
# 49    50     62383     55809   -11%                       2638 WEST NORTH SHORE AVENUE  60645