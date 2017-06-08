DEBUG = False
CONFIG_FILE = '/etc/accountingtables/accountingtables.conf'

PROJECT_STATS_COLUMNS = [
    {
        "data_name": "keys.project_name",
        "column_name": "project_name",
        "default": "",
        "order": 1,
        "searchable": True
    },
    {
        "data_name": "instances_usage.usage",
        "column_name": "instances_usage_usage",
        "default": 0,
        "order": 2,
        "searchable": False
    },
    {
        "data_name": "instances_usage.quota",
        "column_name": "instances_usage_quota",
        "default": 0,
        "order": 3,
        "searchable": False
    },
    {
        "data_name": "instances_usage.percentage",
        "column_name": "instances_usage_percentage",
        "default": 0,
        "order": 4,
        "searchable": False
    },
    {
        "data_name": "cores_usage.usage",
        "column_name": "cores_usage_usage",
        "default": 0,
        "order": 5,
        "searchable": False
    },
    {
        "data_name": "cores_usage.quota",
        "column_name": "cores_usage_quota",
        "default": 0,
        "order": 6,
        "searchable": False
    },
    {
        "data_name": "cores_usage.percentage",
        "column_name": "cores_usage_percentage",
        "default": 0,
        "order": 7,
        "searchable": False
    },
    {
        "data_name": "ram_usage.usage",
        "column_name": "ram_usage_usage",
        "default": 0,
        "order": 8,
        "searchable": False
    },
    {
        "data_name": "ram_usage.quota",
        "column_name": "ram_usage_quota",
        "default": 0,
        "order": 9,
        "searchable": False
    },
    {
        "data_name": "ram_usage.percentage",
        "column_name": "ram_usage_percentage",
        "default": 0,
        "order": 10,
        "searchable": False
    },
    {
        "data_name": "snapshots_usage.usage",
        "column_name": "snapshots_usage_usage",
        "default": 0,
        "order": 11,
        "searchable": False
    },
    {
        "data_name": "snapshots_usage.quota",
        "column_name": "snapshots_usage_quota",
        "default": 0,
        "order": 12,
        "searchable": False
    },
    {
        "data_name": "snapshots_usage.percentage",
        "column_name": "snapshots_usage_percentage",
        "default": 0,
        "order": 13,
        "searchable": False
    },
    {
        "data_name": "volumes_size.usage",
        "column_name": "volumes_size_usage",
        "default": 0,
        "order": 14,
        "searchable": False
    },
    {
        "data_name": "volumes_size.quota",
        "column_name": "volumes_size_quota",
        "default": 0,
        "order": 15,
        "searchable": False
    },
    {
        "data_name": "volumes_size.percentage",
        "column_name": "volumes_size_percentage",
        "default": 0,
        "order": 16,
        "searchable": False
    },
    {
        "data_name": "volumes_usage.usage",
        "column_name": "volumes_usage_usage",
        "default": 0,
        "order": 17,
        "searchable": False
    },
    {
        "data_name": "volumes_usage.quota",
        "column_name": "volumes_usage_quota",
        "default": 0,
        "order": 18,
        "searchable": False
    },
    {
        "data_name": "volumes_usage.percentage",
        "column_name": "volumes_usage_percentage",
        "default": 0,
        "order": 19,
        "searchable": False
    }
]
