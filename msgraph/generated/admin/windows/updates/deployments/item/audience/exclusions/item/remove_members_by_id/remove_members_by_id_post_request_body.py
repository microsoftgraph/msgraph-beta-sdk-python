from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RemoveMembersByIdPostRequestBody(AdditionalDataHolder, Parsable):
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
        Instantiates a new removeMembersByIdPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The ids property
        self._ids: Optional[List[str]] = None
        # The memberEntityType property
        self._member_entity_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoveMembersByIdPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoveMembersByIdPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoveMembersByIdPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ids": lambda n : setattr(self, 'ids', n.get_collection_of_primitive_values(str)),
            "member_entity_type": lambda n : setattr(self, 'member_entity_type', n.get_str_value()),
        }
        return fields
    
    @property
    def ids(self,) -> Optional[List[str]]:
        """
        Gets the ids property value. The ids property
        Returns: Optional[List[str]]
        """
        return self._ids
    
    @ids.setter
    def ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the ids property value. The ids property
        Args:
            value: Value to set for the ids property.
        """
        self._ids = value
    
    @property
    def member_entity_type(self,) -> Optional[str]:
        """
        Gets the memberEntityType property value. The memberEntityType property
        Returns: Optional[str]
        """
        return self._member_entity_type
    
    @member_entity_type.setter
    def member_entity_type(self,value: Optional[str] = None) -> None:
        """
        Sets the memberEntityType property value. The memberEntityType property
        Args:
            value: Value to set for the memberEntityType property.
        """
        self._member_entity_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("ids", self.ids)
        writer.write_str_value("memberEntityType", self.member_entity_type)
        writer.write_additional_data_value(self.additional_data)
    

