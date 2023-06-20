from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_condition_application

@dataclass
class AuthenticationConditionsApplications(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Whether the custom authentication extension should trigger for all applications with appIds specified in the includeApplications relationship. This property must be set to false for listener of type onTokenIssuanceStartListener.
    include_all_applications: Optional[bool] = None
    # The includeApplications property
    include_applications: Optional[List[authentication_condition_application.AuthenticationConditionApplication]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationConditionsApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import authentication_condition_application

        from . import authentication_condition_application

        fields: Dict[str, Callable[[Any], None]] = {
            "includeAllApplications": lambda n : setattr(self, 'include_all_applications', n.get_bool_value()),
            "includeApplications": lambda n : setattr(self, 'include_applications', n.get_collection_of_object_values(authentication_condition_application.AuthenticationConditionApplication)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("includeAllApplications", self.include_all_applications)
        writer.write_collection_of_object_values("includeApplications", self.include_applications)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

