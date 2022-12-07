from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceManagementConfigurationDependentOn(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationDependentOn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identifier of parent setting/ parent setting option dependent on
        self._dependent_on: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Identifier of parent setting/ parent setting id dependent on
        self._parent_setting_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationDependentOn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationDependentOn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationDependentOn()
    
    @property
    def dependent_on(self,) -> Optional[str]:
        """
        Gets the dependentOn property value. Identifier of parent setting/ parent setting option dependent on
        Returns: Optional[str]
        """
        return self._dependent_on
    
    @dependent_on.setter
    def dependent_on(self,value: Optional[str] = None) -> None:
        """
        Sets the dependentOn property value. Identifier of parent setting/ parent setting option dependent on
        Args:
            value: Value to set for the dependentOn property.
        """
        self._dependent_on = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "dependent_on": lambda n : setattr(self, 'dependent_on', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parent_setting_id": lambda n : setattr(self, 'parent_setting_id', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def parent_setting_id(self,) -> Optional[str]:
        """
        Gets the parentSettingId property value. Identifier of parent setting/ parent setting id dependent on
        Returns: Optional[str]
        """
        return self._parent_setting_id
    
    @parent_setting_id.setter
    def parent_setting_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentSettingId property value. Identifier of parent setting/ parent setting id dependent on
        Args:
            value: Value to set for the parentSettingId property.
        """
        self._parent_setting_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("dependentOn", self.dependent_on)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("parentSettingId", self.parent_setting_id)
        writer.write_additional_data_value(self.additional_data)
    

