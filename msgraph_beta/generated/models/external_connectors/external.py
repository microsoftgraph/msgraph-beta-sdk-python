from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..authorization_system import AuthorizationSystem
    from ..industry_data.industry_data_root import IndustryDataRoot
    from .external_connection import ExternalConnection

@dataclass
class External(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Represents an onboarded Amazon Web Services (AWS) account, Azure subscription, or Google Cloud Platform (GCP) project that Microsoft Entra Permissions Management collects and analyzes permissions and actions on.
    authorization_systems: Optional[list[AuthorizationSystem]] = None
    # The connections property
    connections: Optional[list[ExternalConnection]] = None
    # The industryData property
    industry_data: Optional[IndustryDataRoot] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> External:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: External
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return External()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..authorization_system import AuthorizationSystem
        from ..industry_data.industry_data_root import IndustryDataRoot
        from .external_connection import ExternalConnection

        from ..authorization_system import AuthorizationSystem
        from ..industry_data.industry_data_root import IndustryDataRoot
        from .external_connection import ExternalConnection

        fields: dict[str, Callable[[Any], None]] = {
            "authorizationSystems": lambda n : setattr(self, 'authorization_systems', n.get_collection_of_object_values(AuthorizationSystem)),
            "connections": lambda n : setattr(self, 'connections', n.get_collection_of_object_values(ExternalConnection)),
            "industryData": lambda n : setattr(self, 'industry_data', n.get_object_value(IndustryDataRoot)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("authorizationSystems", self.authorization_systems)
        writer.write_collection_of_object_values("connections", self.connections)
        writer.write_object_value("industryData", self.industry_data)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

