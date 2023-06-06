from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attachment, reference_attachment_permission, reference_attachment_provider

from . import attachment

@dataclass
class ReferenceAttachment(attachment.Attachment):
    odata_type = "#microsoft.graph.referenceAttachment"
    # Specifies whether the attachment is a link to a folder. Must set this to true if sourceUrl is a link to a folder. Optional.
    is_folder: Optional[bool] = None
    # Specifies the permissions granted for the attachment by the type of provider in providerType. Possible values are: other, view, edit, anonymousView, anonymousEdit, organizationView, organizationEdit. Optional.
    permission: Optional[reference_attachment_permission.ReferenceAttachmentPermission] = None
    # Applies to only a reference attachment of an image - URL to get a preview image. Use thumbnailUrl and previewUrl only when sourceUrl identifies an image file. Optional.
    preview_url: Optional[str] = None
    # The type of provider that supports an attachment of this contentType. Possible values are: other, oneDriveBusiness, oneDriveConsumer, dropbox. Optional.
    provider_type: Optional[reference_attachment_provider.ReferenceAttachmentProvider] = None
    # URL to get the attachment content. If this is a URL to a folder, then for the folder to be displayed correctly in Outlook or Outlook on the web, set isFolder to true. Required.
    source_url: Optional[str] = None
    # Applies to only a reference attachment of an image - URL to get a thumbnail image. Use thumbnailUrl and previewUrl only when sourceUrl identifies an image file. Optional.
    thumbnail_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReferenceAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReferenceAttachment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReferenceAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attachment, reference_attachment_permission, reference_attachment_provider

        fields: Dict[str, Callable[[Any], None]] = {
            "isFolder": lambda n : setattr(self, 'is_folder', n.get_bool_value()),
            "permission": lambda n : setattr(self, 'permission', n.get_enum_value(reference_attachment_permission.ReferenceAttachmentPermission)),
            "previewUrl": lambda n : setattr(self, 'preview_url', n.get_str_value()),
            "providerType": lambda n : setattr(self, 'provider_type', n.get_enum_value(reference_attachment_provider.ReferenceAttachmentProvider)),
            "sourceUrl": lambda n : setattr(self, 'source_url', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isFolder", self.is_folder)
        writer.write_enum_value("permission", self.permission)
        writer.write_str_value("previewUrl", self.preview_url)
        writer.write_enum_value("providerType", self.provider_type)
        writer.write_str_value("sourceUrl", self.source_url)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
    

