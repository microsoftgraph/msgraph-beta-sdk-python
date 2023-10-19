from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_condition_application import AuthenticationConditionApplication

@dataclass
class AuthenticationConditionsApplications(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Whether the custom authentication extension should trigger for all applications with appIds specified in the includeApplications relationship. This property must be set to false for listener of type onTokenIssuanceStartListener.
    include_all_applications: Optional[bool] = None
    # The includeApplications property
    include_applications: Optional[List[AuthenticationConditionApplication]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationConditionsApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationConditionsApplications
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationConditionsApplications()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_condition_application import AuthenticationConditionApplication

        from .authentication_condition_application import AuthenticationConditionApplication

        fields: Dict[str, Callable[[Any], None]] = {
            "includeAllApplications": lambda n : setattr(self, 'include_all_applications', n.get_bool_value()),
            "includeApplications": lambda n : setattr(self, 'include_applications', n.get_collection_of_object_values(AuthenticationConditionApplication)),
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
        writer.write_bool_value("includeAllApplications", self.include_all_applications)
        writer.write_collection_of_object_values("includeApplications", self.include_applications)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

