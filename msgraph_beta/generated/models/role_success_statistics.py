from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class RoleSuccessStatistics(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The permanentFail property
    permanent_fail: Optional[int] = None
    # The permanentSuccess property
    permanent_success: Optional[int] = None
    # The removeFail property
    remove_fail: Optional[int] = None
    # The removeSuccess property
    remove_success: Optional[int] = None
    # The roleId property
    role_id: Optional[str] = None
    # The roleName property
    role_name: Optional[str] = None
    # The temporaryFail property
    temporary_fail: Optional[int] = None
    # The temporarySuccess property
    temporary_success: Optional[int] = None
    # The unknownFail property
    unknown_fail: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoleSuccessStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoleSuccessStatistics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoleSuccessStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permanentFail": lambda n : setattr(self, 'permanent_fail', n.get_int_value()),
            "permanentSuccess": lambda n : setattr(self, 'permanent_success', n.get_int_value()),
            "removeFail": lambda n : setattr(self, 'remove_fail', n.get_int_value()),
            "removeSuccess": lambda n : setattr(self, 'remove_success', n.get_int_value()),
            "roleId": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "roleName": lambda n : setattr(self, 'role_name', n.get_str_value()),
            "temporaryFail": lambda n : setattr(self, 'temporary_fail', n.get_int_value()),
            "temporarySuccess": lambda n : setattr(self, 'temporary_success', n.get_int_value()),
            "unknownFail": lambda n : setattr(self, 'unknown_fail', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("permanentFail", self.permanent_fail)
        writer.write_int_value("permanentSuccess", self.permanent_success)
        writer.write_int_value("removeFail", self.remove_fail)
        writer.write_int_value("removeSuccess", self.remove_success)
        writer.write_str_value("roleId", self.role_id)
        writer.write_str_value("roleName", self.role_name)
        writer.write_int_value("temporaryFail", self.temporary_fail)
        writer.write_int_value("temporarySuccess", self.temporary_success)
        writer.write_int_value("unknownFail", self.unknown_fail)
        writer.write_additional_data_value(self.additional_data)
    

