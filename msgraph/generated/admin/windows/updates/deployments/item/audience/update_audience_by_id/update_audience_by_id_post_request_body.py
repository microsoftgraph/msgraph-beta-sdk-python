from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UpdateAudienceByIdPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the updateAudienceById method.
    """
    @property
    def add_exclusions(self,) -> Optional[List[str]]:
        """
        Gets the addExclusions property value. The addExclusions property
        Returns: Optional[List[str]]
        """
        return self._add_exclusions
    
    @add_exclusions.setter
    def add_exclusions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the addExclusions property value. The addExclusions property
        Args:
            value: Value to set for the addExclusions property.
        """
        self._add_exclusions = value
    
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
    
    @property
    def add_members(self,) -> Optional[List[str]]:
        """
        Gets the addMembers property value. The addMembers property
        Returns: Optional[List[str]]
        """
        return self._add_members
    
    @add_members.setter
    def add_members(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the addMembers property value. The addMembers property
        Args:
            value: Value to set for the addMembers property.
        """
        self._add_members = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new updateAudienceByIdPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The addExclusions property
        self._add_exclusions: Optional[List[str]] = None
        # The addMembers property
        self._add_members: Optional[List[str]] = None
        # The memberEntityType property
        self._member_entity_type: Optional[str] = None
        # The removeExclusions property
        self._remove_exclusions: Optional[List[str]] = None
        # The removeMembers property
        self._remove_members: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateAudienceByIdPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateAudienceByIdPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateAudienceByIdPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "add_exclusions": lambda n : setattr(self, 'add_exclusions', n.get_collection_of_primitive_values(str)),
            "add_members": lambda n : setattr(self, 'add_members', n.get_collection_of_primitive_values(str)),
            "member_entity_type": lambda n : setattr(self, 'member_entity_type', n.get_str_value()),
            "remove_exclusions": lambda n : setattr(self, 'remove_exclusions', n.get_collection_of_primitive_values(str)),
            "remove_members": lambda n : setattr(self, 'remove_members', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
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
    
    @property
    def remove_exclusions(self,) -> Optional[List[str]]:
        """
        Gets the removeExclusions property value. The removeExclusions property
        Returns: Optional[List[str]]
        """
        return self._remove_exclusions
    
    @remove_exclusions.setter
    def remove_exclusions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the removeExclusions property value. The removeExclusions property
        Args:
            value: Value to set for the removeExclusions property.
        """
        self._remove_exclusions = value
    
    @property
    def remove_members(self,) -> Optional[List[str]]:
        """
        Gets the removeMembers property value. The removeMembers property
        Returns: Optional[List[str]]
        """
        return self._remove_members
    
    @remove_members.setter
    def remove_members(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the removeMembers property value. The removeMembers property
        Args:
            value: Value to set for the removeMembers property.
        """
        self._remove_members = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("addExclusions", self.add_exclusions)
        writer.write_collection_of_primitive_values("addMembers", self.add_members)
        writer.write_str_value("memberEntityType", self.member_entity_type)
        writer.write_collection_of_primitive_values("removeExclusions", self.remove_exclusions)
        writer.write_collection_of_primitive_values("removeMembers", self.remove_members)
        writer.write_additional_data_value(self.additional_data)
    

