from sushy.resources import base
from sushy import utils

from rsd_lib import base as rsd_lib_base

# from  import entries


from rsd_lib import utils as rsd_lib_utils


class LogService(rsd_lib_base.ResourceBase):
    """LogService resource class

       This resource represents the log service for the resource or service to
       which it is associated.
    """

    service_enabled = base.Field("ServiceEnabled", adapter=bool)
    """This indicates whether this service is enabled."""

    max_number_of_records = base.Field(
        "MaxNumberOfRecords", adapter=rsd_lib_utils.num_or_none
    )
    """The maximum number of log entries this service can have."""

    over_write_policy = base.Field("OverWritePolicy")
    """The overwrite policy for this service that takes place when the log is
       full.
    """

    date_time = base.Field("DateTime")
    """The current DateTime (with offset) for the log service, used to set or
       read time.
    """

    date_time_local_offset = base.Field("DateTimeLocalOffset")
    """The time offset from UTC that the DateTime property is set to in
       format: +06:00 .
    """

    status = rsd_lib_base.StatusField("Status")
    """This indicates the known state of the resource, such as if it is
       enabled.
    """

    # TODO(linyang): Add Action Field

    @property
    @utils.cache_it
    def entries(self):
        """Property to provide reference to `LogEntryCollection` instance

           It is calculated once when it is queried for the first time. On
           refresh, this property is reset.
        """
        return log_entry.LogEntryCollection(
            self._conn,
            utils.get_sub_resource_path_by(self, "Entries"),
            redfish_version=self.redfish_version,
        )


class LogServiceCollection(rsd_lib_base.ResourceCollectionBase):
    @property
    def _resource_type(self):
        return LogService
