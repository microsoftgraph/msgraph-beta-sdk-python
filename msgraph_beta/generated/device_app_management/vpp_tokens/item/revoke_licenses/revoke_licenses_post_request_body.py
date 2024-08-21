from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class RevokeLicensesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The notifyManagedDevices property
    notify_managed_devices: Optional[bool] = None
    # The revokeUntrackedLicenses property
    revoke_untracked_licenses: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RevokeLicensesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RevokeLicensesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RevokeLicensesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "notifyManagedDevices": lambda n : setattr(self, 'notify_managed_devices', n.get_bool_value()),
            "revokeUntrackedLicenses": lambda n : setattr(self, 'revoke_untracked_licenses', n.get_bool_value()),
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
        writer.write_bool_value("notifyManagedDevices", self.notify_managed_devices)
        writer.write_bool_value("revokeUntrackedLicenses", self.revoke_untracked_licenses)
        writer.write_additional_data_value(self.additional_data)
    

