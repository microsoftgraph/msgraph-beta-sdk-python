from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identifier_type_reference_value, role_group, user_match_target_reference_value

class UserMatchingSetting(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new userMatchingSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The RefUserMatchTarget for matching a user from the source with an Azure Active Directory user object.
        self._match_target: Optional[user_match_target_reference_value.UserMatchTargetReferenceValue] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The priority order to apply when a user has multiple RefRole codes assigned.
        self._priority_order: Optional[int] = None
        # The roleGroup property
        self._role_group: Optional[role_group.RoleGroup] = None
        # The sourceIdentifier property
        self._source_identifier: Optional[identifier_type_reference_value.IdentifierTypeReferenceValue] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserMatchingSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserMatchingSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserMatchingSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identifier_type_reference_value, role_group, user_match_target_reference_value

        fields: Dict[str, Callable[[Any], None]] = {
            "matchTarget": lambda n : setattr(self, 'match_target', n.get_object_value(user_match_target_reference_value.UserMatchTargetReferenceValue)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priorityOrder": lambda n : setattr(self, 'priority_order', n.get_int_value()),
            "roleGroup": lambda n : setattr(self, 'role_group', n.get_object_value(role_group.RoleGroup)),
            "sourceIdentifier": lambda n : setattr(self, 'source_identifier', n.get_object_value(identifier_type_reference_value.IdentifierTypeReferenceValue)),
        }
        return fields
    
    @property
    def match_target(self,) -> Optional[user_match_target_reference_value.UserMatchTargetReferenceValue]:
        """
        Gets the matchTarget property value. The RefUserMatchTarget for matching a user from the source with an Azure Active Directory user object.
        Returns: Optional[user_match_target_reference_value.UserMatchTargetReferenceValue]
        """
        return self._match_target
    
    @match_target.setter
    def match_target(self,value: Optional[user_match_target_reference_value.UserMatchTargetReferenceValue] = None) -> None:
        """
        Sets the matchTarget property value. The RefUserMatchTarget for matching a user from the source with an Azure Active Directory user object.
        Args:
            value: Value to set for the match_target property.
        """
        self._match_target = value
    
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
    def priority_order(self,) -> Optional[int]:
        """
        Gets the priorityOrder property value. The priority order to apply when a user has multiple RefRole codes assigned.
        Returns: Optional[int]
        """
        return self._priority_order
    
    @priority_order.setter
    def priority_order(self,value: Optional[int] = None) -> None:
        """
        Sets the priorityOrder property value. The priority order to apply when a user has multiple RefRole codes assigned.
        Args:
            value: Value to set for the priority_order property.
        """
        self._priority_order = value
    
    @property
    def role_group(self,) -> Optional[role_group.RoleGroup]:
        """
        Gets the roleGroup property value. The roleGroup property
        Returns: Optional[role_group.RoleGroup]
        """
        return self._role_group
    
    @role_group.setter
    def role_group(self,value: Optional[role_group.RoleGroup] = None) -> None:
        """
        Sets the roleGroup property value. The roleGroup property
        Args:
            value: Value to set for the role_group property.
        """
        self._role_group = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("matchTarget", self.match_target)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("priorityOrder", self.priority_order)
        writer.write_object_value("roleGroup", self.role_group)
        writer.write_object_value("sourceIdentifier", self.source_identifier)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_identifier(self,) -> Optional[identifier_type_reference_value.IdentifierTypeReferenceValue]:
        """
        Gets the sourceIdentifier property value. The sourceIdentifier property
        Returns: Optional[identifier_type_reference_value.IdentifierTypeReferenceValue]
        """
        return self._source_identifier
    
    @source_identifier.setter
    def source_identifier(self,value: Optional[identifier_type_reference_value.IdentifierTypeReferenceValue] = None) -> None:
        """
        Sets the sourceIdentifier property value. The sourceIdentifier property
        Args:
            value: Value to set for the source_identifier property.
        """
        self._source_identifier = value
    

