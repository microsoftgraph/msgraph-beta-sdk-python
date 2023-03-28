from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ConditionalAccessLocations(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessLocations and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Location IDs excluded from scope of policy.
        self._exclude_locations: Optional[List[str]] = None
        # Location IDs in scope of policy unless explicitly excluded, All, or AllTrusted.
        self._include_locations: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessLocations:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessLocations
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessLocations()
    
    @property
    def exclude_locations(self,) -> Optional[List[str]]:
        """
        Gets the excludeLocations property value. Location IDs excluded from scope of policy.
        Returns: Optional[List[str]]
        """
        return self._exclude_locations
    
    @exclude_locations.setter
    def exclude_locations(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeLocations property value. Location IDs excluded from scope of policy.
        Args:
            value: Value to set for the exclude_locations property.
        """
        self._exclude_locations = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "excludeLocations": lambda n : setattr(self, 'exclude_locations', n.get_collection_of_primitive_values(str)),
            "includeLocations": lambda n : setattr(self, 'include_locations', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def include_locations(self,) -> Optional[List[str]]:
        """
        Gets the includeLocations property value. Location IDs in scope of policy unless explicitly excluded, All, or AllTrusted.
        Returns: Optional[List[str]]
        """
        return self._include_locations
    
    @include_locations.setter
    def include_locations(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeLocations property value. Location IDs in scope of policy unless explicitly excluded, All, or AllTrusted.
        Args:
            value: Value to set for the include_locations property.
        """
        self._include_locations = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_collection_of_primitive_values("excludeLocations", self.exclude_locations)
        writer.write_collection_of_primitive_values("includeLocations", self.include_locations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

