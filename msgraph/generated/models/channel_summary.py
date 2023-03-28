from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ChannelSummary(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new channelSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The guestsCount property
        self._guests_count: Optional[int] = None
        # The hasMembersFromOtherTenants property
        self._has_members_from_other_tenants: Optional[bool] = None
        # The membersCount property
        self._members_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ownersCount property
        self._owners_count: Optional[int] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChannelSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChannelSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChannelSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "guestsCount": lambda n : setattr(self, 'guests_count', n.get_int_value()),
            "hasMembersFromOtherTenants": lambda n : setattr(self, 'has_members_from_other_tenants', n.get_bool_value()),
            "membersCount": lambda n : setattr(self, 'members_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ownersCount": lambda n : setattr(self, 'owners_count', n.get_int_value()),
        }
        return fields
    
    @property
    def guests_count(self,) -> Optional[int]:
        """
        Gets the guestsCount property value. The guestsCount property
        Returns: Optional[int]
        """
        return self._guests_count
    
    @guests_count.setter
    def guests_count(self,value: Optional[int] = None) -> None:
        """
        Sets the guestsCount property value. The guestsCount property
        Args:
            value: Value to set for the guests_count property.
        """
        self._guests_count = value
    
    @property
    def has_members_from_other_tenants(self,) -> Optional[bool]:
        """
        Gets the hasMembersFromOtherTenants property value. The hasMembersFromOtherTenants property
        Returns: Optional[bool]
        """
        return self._has_members_from_other_tenants
    
    @has_members_from_other_tenants.setter
    def has_members_from_other_tenants(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasMembersFromOtherTenants property value. The hasMembersFromOtherTenants property
        Args:
            value: Value to set for the has_members_from_other_tenants property.
        """
        self._has_members_from_other_tenants = value
    
    @property
    def members_count(self,) -> Optional[int]:
        """
        Gets the membersCount property value. The membersCount property
        Returns: Optional[int]
        """
        return self._members_count
    
    @members_count.setter
    def members_count(self,value: Optional[int] = None) -> None:
        """
        Sets the membersCount property value. The membersCount property
        Args:
            value: Value to set for the members_count property.
        """
        self._members_count = value
    
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
    def owners_count(self,) -> Optional[int]:
        """
        Gets the ownersCount property value. The ownersCount property
        Returns: Optional[int]
        """
        return self._owners_count
    
    @owners_count.setter
    def owners_count(self,value: Optional[int] = None) -> None:
        """
        Sets the ownersCount property value. The ownersCount property
        Args:
            value: Value to set for the owners_count property.
        """
        self._owners_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("guestsCount", self.guests_count)
        writer.write_bool_value("hasMembersFromOtherTenants", self.has_members_from_other_tenants)
        writer.write_int_value("membersCount", self.members_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("ownersCount", self.owners_count)
        writer.write_additional_data_value(self.additional_data)
    

