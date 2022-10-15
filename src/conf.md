# Configuration
Redundancy-Maker is configurable in order to best suit your needs/your hardware constrains.

|Keyword|Description|Required|Default|Additional Info|
|-------|-----------|:------:|:-----:|---------------|
|`target_directory`|the directory that you want to backup|yes|-|-|
|`mirror_directory`|the directory that in which you will clone your `target_direcotry`|yes|-|at firs lauch this directory **must be empty**|
|`cpu_load_threshold`|set the maximum cpu load where the tool can run |no|35|set the value accordingly to your cpu power. Recommended between 20 and 60. Integer required.|
|`cpu_scan_time`|time expressed in *minutes* needed to probe the cpu (to determin load)|no|5|increasing this value can reduce overall load of your cpu but increases inaccuracy. Integer required.|
|`cpu_rescan_interval`|time expressed in *minutes* between two different cpu scan|no|10|"  "  "|
|`filesystem_watch_timeout`|minimum time, expressed in *minutes*, between two different scans of `target_dir`|no|15|increasing this value can reduce overall load of your cpu but syncs occurs less often. Integer required.|
|`logger`|set if output shuold be logged in file `rm_log.txt`|no|False|advised to be enable on first lauch of the tool(if works corrctly can be disabled). Required in case of bug report|