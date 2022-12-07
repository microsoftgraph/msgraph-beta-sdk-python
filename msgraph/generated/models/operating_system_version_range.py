from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class OperatingSystemVersionRange(AdditionalDataHolder, Parsable):
    """
    Operating System version range.
    """
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
        Instantiates a new operatingSystemVersionRange and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The description of this range (e.g. Valid 1702 builds)
        self._description: Optional[str] = None
        # The highest inclusive version that this range contains.
        self._highest_version: Optional[str] = None
        # The lowest inclusive version that this range contains.
        self._lowest_version: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OperatingSystemVersionRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OperatingSystemVersionRange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OperatingSystemVersionRange()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of this range (e.g. Valid 1702 builds)
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of this range (e.g. Valid 1702 builds)
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "highest_version": lambda n : setattr(self, 'highest_version', n.get_str_value()),
            "lowest_version": lambda n : setattr(self, 'lowest_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def highest_version(self,) -> Optional[str]:
        """
        Gets the highestVersion property value. The highest inclusive version that this range contains.
        Returns: Optional[str]
        """
        return self._highest_version
    
    @highest_version.setter
    def highest_version(self,value: Optional[str] = None) -> None:
        """
        Sets the highestVersion property value. The highest inclusive version that this range contains.
        Args:
            value: Value to set for the highestVersion property.
        """
        self._highest_version = value
    
    @property
    def lowest_version(self,) -> Optional[str]:
        """
        Gets the lowestVersion property value. The lowest inclusive version that this range contains.
        Returns: Optional[str]
        """
        return self._lowest_version
    
    @lowest_version.setter
    def lowest_version(self,value: Optional[str] = None) -> None:
        """
        Sets the lowestVersion property value. The lowest inclusive version that this range contains.
        Args:
            value: Value to set for the lowestVersion property.
        """
        self._lowest_version = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_str_value("highestVersion", self.highest_version)
        writer.write_str_value("lowestVersion", self.lowest_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

