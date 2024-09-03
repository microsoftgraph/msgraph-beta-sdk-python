from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AdditionalClassGroupOptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether a team should be created for the class group.
    create_team: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the class group display name should be set on create.
    write_display_name_on_create_only: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdditionalClassGroupOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdditionalClassGroupOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdditionalClassGroupOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "createTeam": lambda n : setattr(self, 'create_team', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "writeDisplayNameOnCreateOnly": lambda n : setattr(self, 'write_display_name_on_create_only', n.get_bool_value()),
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
        writer.write_bool_value("createTeam", self.create_team)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("writeDisplayNameOnCreateOnly", self.write_display_name_on_create_only)
        writer.write_additional_data_value(self.additional_data)
    

