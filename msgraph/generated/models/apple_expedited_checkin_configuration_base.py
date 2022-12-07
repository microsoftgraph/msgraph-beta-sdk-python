from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class AppleExpeditedCheckinConfigurationBase(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AppleExpeditedCheckinConfigurationBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.appleExpeditedCheckinConfigurationBase"
        # Gets or sets whether to enable expedited device check-ins.
        self._enable_expedited_checkin: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleExpeditedCheckinConfigurationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleExpeditedCheckinConfigurationBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppleExpeditedCheckinConfigurationBase()
    
    @property
    def enable_expedited_checkin(self,) -> Optional[bool]:
        """
        Gets the enableExpeditedCheckin property value. Gets or sets whether to enable expedited device check-ins.
        Returns: Optional[bool]
        """
        return self._enable_expedited_checkin
    
    @enable_expedited_checkin.setter
    def enable_expedited_checkin(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableExpeditedCheckin property value. Gets or sets whether to enable expedited device check-ins.
        Args:
            value: Value to set for the enableExpeditedCheckin property.
        """
        self._enable_expedited_checkin = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enable_expedited_checkin": lambda n : setattr(self, 'enable_expedited_checkin', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("enableExpeditedCheckin", self.enable_expedited_checkin)
    

