from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sharing_link_expiration_status import SharingLinkExpirationStatus
    from .sharing_link_variants import SharingLinkVariants
    from .sharing_operation_status import SharingOperationStatus

@dataclass
class LinkRoleAbilities(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates if the current user can add existing external user recipients to this sharing link.
    add_existing_external_users: Optional[SharingOperationStatus] = None
    # Indicates if the current user can add new external user recipients to this sharing link.
    add_new_external_users: Optional[SharingOperationStatus] = None
    # Indicates the status of the potential sharing link variants. If selected, it generates a separate sharing link from the sharing link that would otherwise be generated without the variant, yet with an identical role and scope.
    apply_variants: Optional[SharingLinkVariants] = None
    # Indicates if links of this role can be created.
    create_link: Optional[SharingOperationStatus] = None
    # Indicates if links of this role can be deleted.
    delete_link: Optional[SharingOperationStatus] = None
    # Indicates if this link can include external users.
    link_allows_external_users: Optional[SharingOperationStatus] = None
    # Indicates if links must expire, meaning the link is no longer usable after a specified time. If link expiration is enabled, a default link expiration time is provided.
    link_expiration: Optional[SharingLinkExpirationStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates if links of this role can be retrieved.
    retrieve_link: Optional[SharingOperationStatus] = None
    # Indicates if links of this role can be updated.
    update_link: Optional[SharingOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LinkRoleAbilities:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LinkRoleAbilities
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LinkRoleAbilities()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .sharing_link_expiration_status import SharingLinkExpirationStatus
        from .sharing_link_variants import SharingLinkVariants
        from .sharing_operation_status import SharingOperationStatus

        from .sharing_link_expiration_status import SharingLinkExpirationStatus
        from .sharing_link_variants import SharingLinkVariants
        from .sharing_operation_status import SharingOperationStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "addExistingExternalUsers": lambda n : setattr(self, 'add_existing_external_users', n.get_object_value(SharingOperationStatus)),
            "addNewExternalUsers": lambda n : setattr(self, 'add_new_external_users', n.get_object_value(SharingOperationStatus)),
            "applyVariants": lambda n : setattr(self, 'apply_variants', n.get_object_value(SharingLinkVariants)),
            "createLink": lambda n : setattr(self, 'create_link', n.get_object_value(SharingOperationStatus)),
            "deleteLink": lambda n : setattr(self, 'delete_link', n.get_object_value(SharingOperationStatus)),
            "linkAllowsExternalUsers": lambda n : setattr(self, 'link_allows_external_users', n.get_object_value(SharingOperationStatus)),
            "linkExpiration": lambda n : setattr(self, 'link_expiration', n.get_object_value(SharingLinkExpirationStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "retrieveLink": lambda n : setattr(self, 'retrieve_link', n.get_object_value(SharingOperationStatus)),
            "updateLink": lambda n : setattr(self, 'update_link', n.get_object_value(SharingOperationStatus)),
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
        writer.write_object_value("addExistingExternalUsers", self.add_existing_external_users)
        writer.write_object_value("addNewExternalUsers", self.add_new_external_users)
        writer.write_object_value("applyVariants", self.apply_variants)
        writer.write_object_value("createLink", self.create_link)
        writer.write_object_value("deleteLink", self.delete_link)
        writer.write_object_value("linkAllowsExternalUsers", self.link_allows_external_users)
        writer.write_object_value("linkExpiration", self.link_expiration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("retrieveLink", self.retrieve_link)
        writer.write_object_value("updateLink", self.update_link)
        writer.write_additional_data_value(self.additional_data)
    

