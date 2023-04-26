from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_setting_insights_definition, entity

from . import entity

class DeviceManagementTemplateInsightsDefinition(entity.Entity):
    """
    template insights definition
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementTemplateInsightsDefinition and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Setting insights in a template
        self._setting_insights: Optional[List[device_management_setting_insights_definition.DeviceManagementSettingInsightsDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementTemplateInsightsDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTemplateInsightsDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementTemplateInsightsDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_setting_insights_definition, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "settingInsights": lambda n : setattr(self, 'setting_insights', n.get_collection_of_object_values(device_management_setting_insights_definition.DeviceManagementSettingInsightsDefinition)),
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
        writer.write_collection_of_object_values("settingInsights", self.setting_insights)
    
    @property
    def setting_insights(self,) -> Optional[List[device_management_setting_insights_definition.DeviceManagementSettingInsightsDefinition]]:
        """
        Gets the settingInsights property value. Setting insights in a template
        Returns: Optional[List[device_management_setting_insights_definition.DeviceManagementSettingInsightsDefinition]]
        """
        return self._setting_insights
    
    @setting_insights.setter
    def setting_insights(self,value: Optional[List[device_management_setting_insights_definition.DeviceManagementSettingInsightsDefinition]] = None) -> None:
        """
        Sets the settingInsights property value. Setting insights in a template
        Args:
            value: Value to set for the setting_insights property.
        """
        self._setting_insights = value
    

