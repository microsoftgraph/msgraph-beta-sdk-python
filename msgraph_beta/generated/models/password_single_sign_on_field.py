from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PasswordSingleSignOnField(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Title/label override for customization.
    customized_label: Optional[str] = None
    # Label that would be used if no customizedLabel is provided. Read only.
    default_label: Optional[str] = None
    # Id used to identity the field type. This is an internal ID and possible values are param1, param2, paramuserName, parampassword.
    field_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of the credential. The values can be text, password.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasswordSingleSignOnField:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasswordSingleSignOnField
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasswordSingleSignOnField()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "customizedLabel": lambda n : setattr(self, 'customized_label', n.get_str_value()),
            "defaultLabel": lambda n : setattr(self, 'default_label', n.get_str_value()),
            "fieldId": lambda n : setattr(self, 'field_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("customizedLabel", self.customized_label)
        writer.write_str_value("defaultLabel", self.default_label)
        writer.write_str_value("fieldId", self.field_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

