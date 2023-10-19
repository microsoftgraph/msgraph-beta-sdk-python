from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_account_configuration import TeamworkAccountConfiguration
    from .teamwork_features_configuration import TeamworkFeaturesConfiguration

@dataclass
class TeamworkTeamsClientConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The configuration of the Microsoft Teams client user account for a device.
    account_configuration: Optional[TeamworkAccountConfiguration] = None
    # The configuration of Microsoft Teams client features for a device.
    features_configuration: Optional[TeamworkFeaturesConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkTeamsClientConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkTeamsClientConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkTeamsClientConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_account_configuration import TeamworkAccountConfiguration
        from .teamwork_features_configuration import TeamworkFeaturesConfiguration

        from .teamwork_account_configuration import TeamworkAccountConfiguration
        from .teamwork_features_configuration import TeamworkFeaturesConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "accountConfiguration": lambda n : setattr(self, 'account_configuration', n.get_object_value(TeamworkAccountConfiguration)),
            "featuresConfiguration": lambda n : setattr(self, 'features_configuration', n.get_object_value(TeamworkFeaturesConfiguration)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("accountConfiguration", self.account_configuration)
        writer.write_object_value("featuresConfiguration", self.features_configuration)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

