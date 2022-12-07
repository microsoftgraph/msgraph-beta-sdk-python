from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsImpactingProcess(entity.Entity):
    """
    The user experience analytics top impacting process entity.
    """
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. The category of impacting process.
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. The category of impacting process.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsImpactingProcess and sets the default values.
        """
        super().__init__()
        # The category of impacting process.
        self._category: Optional[str] = None
        # The description of process.
        self._description: Optional[str] = None
        # The unique identifier of the impacted device.
        self._device_id: Optional[str] = None
        # The impact value of the process. Valid values 0 to 1.79769313486232E+308
        self._impact_value: Optional[float] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The process name.
        self._process_name: Optional[str] = None
        # The publisher of the process.
        self._publisher: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsImpactingProcess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsImpactingProcess
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsImpactingProcess()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of process.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of process.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The unique identifier of the impacted device.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The unique identifier of the impacted device.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "impact_value": lambda n : setattr(self, 'impact_value', n.get_float_value()),
            "process_name": lambda n : setattr(self, 'process_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def impact_value(self,) -> Optional[float]:
        """
        Gets the impactValue property value. The impact value of the process. Valid values 0 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._impact_value
    
    @impact_value.setter
    def impact_value(self,value: Optional[float] = None) -> None:
        """
        Sets the impactValue property value. The impact value of the process. Valid values 0 to 1.79769313486232E+308
        Args:
            value: Value to set for the impactValue property.
        """
        self._impact_value = value
    
    @property
    def process_name(self,) -> Optional[str]:
        """
        Gets the processName property value. The process name.
        Returns: Optional[str]
        """
        return self._process_name
    
    @process_name.setter
    def process_name(self,value: Optional[str] = None) -> None:
        """
        Sets the processName property value. The process name.
        Args:
            value: Value to set for the processName property.
        """
        self._process_name = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The publisher of the process.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The publisher of the process.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_float_value("impactValue", self.impact_value)
        writer.write_str_value("processName", self.process_name)
        writer.write_str_value("publisher", self.publisher)
    

