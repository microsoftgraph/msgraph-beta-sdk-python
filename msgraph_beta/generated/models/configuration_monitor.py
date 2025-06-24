from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configuration_baseline import ConfigurationBaseline
    from .entity import Entity
    from .identity_set import IdentitySet
    from .monitor_mode import MonitorMode
    from .monitor_status import MonitorStatus
    from .open_complex_dictionary_type import OpenComplexDictionaryType

from .entity import Entity

@dataclass
class ConfigurationMonitor(Entity, Parsable):
    # The baseline property
    baseline: Optional[ConfigurationBaseline] = None
    # The createdBy property
    created_by: Optional[IdentitySet] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The mode property
    mode: Optional[MonitorMode] = None
    # The monitorRunFrequencyInHours property
    monitor_run_frequency_in_hours: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parameters property
    parameters: Optional[OpenComplexDictionaryType] = None
    # The runningOnBehalfOf property
    running_on_behalf_of: Optional[IdentitySet] = None
    # The status property
    status: Optional[MonitorStatus] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationMonitor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationMonitor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationMonitor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .configuration_baseline import ConfigurationBaseline
        from .entity import Entity
        from .identity_set import IdentitySet
        from .monitor_mode import MonitorMode
        from .monitor_status import MonitorStatus
        from .open_complex_dictionary_type import OpenComplexDictionaryType

        from .configuration_baseline import ConfigurationBaseline
        from .entity import Entity
        from .identity_set import IdentitySet
        from .monitor_mode import MonitorMode
        from .monitor_status import MonitorStatus
        from .open_complex_dictionary_type import OpenComplexDictionaryType

        fields: dict[str, Callable[[Any], None]] = {
            "baseline": lambda n : setattr(self, 'baseline', n.get_object_value(ConfigurationBaseline)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(MonitorMode)),
            "monitorRunFrequencyInHours": lambda n : setattr(self, 'monitor_run_frequency_in_hours', n.get_int_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_object_value(OpenComplexDictionaryType)),
            "runningOnBehalfOf": lambda n : setattr(self, 'running_on_behalf_of', n.get_object_value(IdentitySet)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(MonitorStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("baseline", self.baseline)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("mode", self.mode)
        writer.write_object_value("parameters", self.parameters)
        writer.write_object_value("runningOnBehalfOf", self.running_on_behalf_of)
        writer.write_enum_value("status", self.status)
    

