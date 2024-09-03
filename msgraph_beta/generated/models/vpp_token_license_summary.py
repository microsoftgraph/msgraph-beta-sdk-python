from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class VppTokenLicenseSummary(AdditionalDataHolder, BackedModel, Parsable):
    """
    License summary of a given app in a token.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The Apple Id associated with the given Apple Volume Purchase Program Token.
    apple_id: Optional[str] = None
    # The number of VPP licenses available.
    available_license_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organization associated with the Apple Volume Purchase Program Token.
    organization_name: Optional[str] = None
    # The number of VPP licenses in use.
    used_license_count: Optional[int] = None
    # Identifier of the VPP token.
    vpp_token_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VppTokenLicenseSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VppTokenLicenseSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VppTokenLicenseSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "appleId": lambda n : setattr(self, 'apple_id', n.get_str_value()),
            "availableLicenseCount": lambda n : setattr(self, 'available_license_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
            "vppTokenId": lambda n : setattr(self, 'vpp_token_id', n.get_str_value()),
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
        writer.write_str_value("appleId", self.apple_id)
        writer.write_int_value("availableLicenseCount", self.available_license_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
        writer.write_str_value("vppTokenId", self.vpp_token_id)
        writer.write_additional_data_value(self.additional_data)
    

