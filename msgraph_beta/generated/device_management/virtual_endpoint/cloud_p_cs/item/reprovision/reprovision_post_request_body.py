from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .reprovision_post_request_body_os_version import ReprovisionPostRequestBody_osVersion
    from .reprovision_post_request_body_user_account_type import ReprovisionPostRequestBody_userAccountType

@dataclass
class ReprovisionPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The osVersion property
    os_version: Optional[ReprovisionPostRequestBody_osVersion] = None
    # The userAccountType property
    user_account_type: Optional[ReprovisionPostRequestBody_userAccountType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReprovisionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReprovisionPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ReprovisionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .reprovision_post_request_body_os_version import ReprovisionPostRequestBody_osVersion
        from .reprovision_post_request_body_user_account_type import ReprovisionPostRequestBody_userAccountType

        from .reprovision_post_request_body_os_version import ReprovisionPostRequestBody_osVersion
        from .reprovision_post_request_body_user_account_type import ReprovisionPostRequestBody_userAccountType

        fields: Dict[str, Callable[[Any], None]] = {
            "osVersion": lambda n : setattr(self, 'os_version', n.get_enum_value(ReprovisionPostRequestBody_osVersion)),
            "userAccountType": lambda n : setattr(self, 'user_account_type', n.get_enum_value(ReprovisionPostRequestBody_userAccountType)),
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
        writer.write_enum_value("osVersion", self.os_version)
        writer.write_enum_value("userAccountType", self.user_account_type)
        writer.write_additional_data_value(self.additional_data)
    

