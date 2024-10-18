from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.cloud_certification_authority_status import CloudCertificationAuthorityStatus

@dataclass
class ChangeCloudCertificationAuthorityStatusPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Enum type of possible certification authority statuses. These statuses indicate whether a certification authority is currently able to issue certificates or temporarily paused or permanently revoked.
    certification_authority_status: Optional[CloudCertificationAuthorityStatus] = None
    # The certificationAuthorityVersion property
    certification_authority_version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChangeCloudCertificationAuthorityStatusPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChangeCloudCertificationAuthorityStatusPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChangeCloudCertificationAuthorityStatusPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.cloud_certification_authority_status import CloudCertificationAuthorityStatus

        from .....models.cloud_certification_authority_status import CloudCertificationAuthorityStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "certificationAuthorityStatus": lambda n : setattr(self, 'certification_authority_status', n.get_enum_value(CloudCertificationAuthorityStatus)),
            "certificationAuthorityVersion": lambda n : setattr(self, 'certification_authority_version', n.get_int_value()),
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
        writer.write_enum_value("certificationAuthorityStatus", self.certification_authority_status)
        writer.write_int_value("certificationAuthorityVersion", self.certification_authority_version)
        writer.write_additional_data_value(self.additional_data)
    

