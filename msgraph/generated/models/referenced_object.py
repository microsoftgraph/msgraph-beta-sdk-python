from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ReferencedObject(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new referencedObject and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Name of the referenced object. Must match one of the objects in the directory definition.
        self._referenced_object_name: Optional[str] = None
        # Currently not supported. Name of the property in the referenced object, the value for which is used as the reference.
        self._referenced_property: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReferencedObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReferencedObject
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReferencedObject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "referencedObjectName": lambda n : setattr(self, 'referenced_object_name', n.get_str_value()),
            "referencedProperty": lambda n : setattr(self, 'referenced_property', n.get_str_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def referenced_object_name(self,) -> Optional[str]:
        """
        Gets the referencedObjectName property value. Name of the referenced object. Must match one of the objects in the directory definition.
        Returns: Optional[str]
        """
        return self._referenced_object_name
    
    @referenced_object_name.setter
    def referenced_object_name(self,value: Optional[str] = None) -> None:
        """
        Sets the referencedObjectName property value. Name of the referenced object. Must match one of the objects in the directory definition.
        Args:
            value: Value to set for the referenced_object_name property.
        """
        self._referenced_object_name = value
    
    @property
    def referenced_property(self,) -> Optional[str]:
        """
        Gets the referencedProperty property value. Currently not supported. Name of the property in the referenced object, the value for which is used as the reference.
        Returns: Optional[str]
        """
        return self._referenced_property
    
    @referenced_property.setter
    def referenced_property(self,value: Optional[str] = None) -> None:
        """
        Sets the referencedProperty property value. Currently not supported. Name of the property in the referenced object, the value for which is used as the reference.
        Args:
            value: Value to set for the referenced_property property.
        """
        self._referenced_property = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("referencedObjectName", self.referenced_object_name)
        writer.write_str_value("referencedProperty", self.referenced_property)
        writer.write_additional_data_value(self.additional_data)
    

