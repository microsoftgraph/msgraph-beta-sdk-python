from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .additional_user_attributes import AdditionalUserAttributes
    from .additional_user_options import AdditionalUserOptions

@dataclass
class UserManagementOptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The different attribute choices for the users to be provisioned. The possible values are: userGradeLevel, userNumber, unknownFutureValue.
    additional_attributes: Optional[List[AdditionalUserAttributes]] = None
    # The additionalOptions property
    additional_options: Optional[AdditionalUserOptions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserManagementOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserManagementOptions
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserManagementOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .additional_user_attributes import AdditionalUserAttributes
        from .additional_user_options import AdditionalUserOptions

        from .additional_user_attributes import AdditionalUserAttributes
        from .additional_user_options import AdditionalUserOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalAttributes": lambda n : setattr(self, 'additional_attributes', n.get_collection_of_enum_values(AdditionalUserAttributes)),
            "additionalOptions": lambda n : setattr(self, 'additional_options', n.get_object_value(AdditionalUserOptions)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_enum_values("additionalAttributes", self.additional_attributes)
        writer.write_object_value("additionalOptions", self.additional_options)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

