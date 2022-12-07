from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment = lazy_import('msgraph.generated.models.attachment')
reference_attachment_permission = lazy_import('msgraph.generated.models.reference_attachment_permission')
reference_attachment_provider = lazy_import('msgraph.generated.models.reference_attachment_provider')

class ReferenceAttachment(attachment.Attachment):
    def __init__(self,) -> None:
        """
        Instantiates a new ReferenceAttachment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.referenceAttachment"
        # Specifies whether the attachment is a link to a folder. Must set this to true if sourceUrl is a link to a folder. Optional.
        self._is_folder: Optional[bool] = None
        # Specifies the permissions granted for the attachment by the type of provider in providerType. Possible values are: other, view, edit, anonymousView, anonymousEdit, organizationView, organizationEdit. Optional.
        self._permission: Optional[reference_attachment_permission.ReferenceAttachmentPermission] = None
        # Applies to only a reference attachment of an image - URL to get a preview image. Use thumbnailUrl and previewUrl only when sourceUrl identifies an image file. Optional.
        self._preview_url: Optional[str] = None
        # The type of provider that supports an attachment of this contentType. Possible values are: other, oneDriveBusiness, oneDriveConsumer, dropbox. Optional.
        self._provider_type: Optional[reference_attachment_provider.ReferenceAttachmentProvider] = None
        # URL to get the attachment content. If this is a URL to a folder, then for the folder to be displayed correctly in Outlook or Outlook on the web, set isFolder to true. Required.
        self._source_url: Optional[str] = None
        # Applies to only a reference attachment of an image - URL to get a thumbnail image. Use thumbnailUrl and previewUrl only when sourceUrl identifies an image file. Optional.
        self._thumbnail_url: Optional[str] = None
    
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
        fields = {
            "is_folder": lambda n : setattr(self, 'is_folder', n.get_bool_value()),
            "permission": lambda n : setattr(self, 'permission', n.get_enum_value(reference_attachment_permission.ReferenceAttachmentPermission)),
            "preview_url": lambda n : setattr(self, 'preview_url', n.get_str_value()),
            "provider_type": lambda n : setattr(self, 'provider_type', n.get_enum_value(reference_attachment_provider.ReferenceAttachmentProvider)),
            "source_url": lambda n : setattr(self, 'source_url', n.get_str_value()),
            "thumbnail_url": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_folder(self,) -> Optional[bool]:
        """
        Gets the isFolder property value. Specifies whether the attachment is a link to a folder. Must set this to true if sourceUrl is a link to a folder. Optional.
        Returns: Optional[bool]
        """
        return self._is_folder
    
    @is_folder.setter
    def is_folder(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFolder property value. Specifies whether the attachment is a link to a folder. Must set this to true if sourceUrl is a link to a folder. Optional.
        Args:
            value: Value to set for the isFolder property.
        """
        self._is_folder = value
    
    @property
    def permission(self,) -> Optional[reference_attachment_permission.ReferenceAttachmentPermission]:
        """
        Gets the permission property value. Specifies the permissions granted for the attachment by the type of provider in providerType. Possible values are: other, view, edit, anonymousView, anonymousEdit, organizationView, organizationEdit. Optional.
        Returns: Optional[reference_attachment_permission.ReferenceAttachmentPermission]
        """
        return self._permission
    
    @permission.setter
    def permission(self,value: Optional[reference_attachment_permission.ReferenceAttachmentPermission] = None) -> None:
        """
        Sets the permission property value. Specifies the permissions granted for the attachment by the type of provider in providerType. Possible values are: other, view, edit, anonymousView, anonymousEdit, organizationView, organizationEdit. Optional.
        Args:
            value: Value to set for the permission property.
        """
        self._permission = value
    
    @property
    def preview_url(self,) -> Optional[str]:
        """
        Gets the previewUrl property value. Applies to only a reference attachment of an image - URL to get a preview image. Use thumbnailUrl and previewUrl only when sourceUrl identifies an image file. Optional.
        Returns: Optional[str]
        """
        return self._preview_url
    
    @preview_url.setter
    def preview_url(self,value: Optional[str] = None) -> None:
        """
        Sets the previewUrl property value. Applies to only a reference attachment of an image - URL to get a preview image. Use thumbnailUrl and previewUrl only when sourceUrl identifies an image file. Optional.
        Args:
            value: Value to set for the previewUrl property.
        """
        self._preview_url = value
    
    @property
    def provider_type(self,) -> Optional[reference_attachment_provider.ReferenceAttachmentProvider]:
        """
        Gets the providerType property value. The type of provider that supports an attachment of this contentType. Possible values are: other, oneDriveBusiness, oneDriveConsumer, dropbox. Optional.
        Returns: Optional[reference_attachment_provider.ReferenceAttachmentProvider]
        """
        return self._provider_type
    
    @provider_type.setter
    def provider_type(self,value: Optional[reference_attachment_provider.ReferenceAttachmentProvider] = None) -> None:
        """
        Sets the providerType property value. The type of provider that supports an attachment of this contentType. Possible values are: other, oneDriveBusiness, oneDriveConsumer, dropbox. Optional.
        Args:
            value: Value to set for the providerType property.
        """
        self._provider_type = value
    
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
    
    @property
    def source_url(self,) -> Optional[str]:
        """
        Gets the sourceUrl property value. URL to get the attachment content. If this is a URL to a folder, then for the folder to be displayed correctly in Outlook or Outlook on the web, set isFolder to true. Required.
        Returns: Optional[str]
        """
        return self._source_url
    
    @source_url.setter
    def source_url(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceUrl property value. URL to get the attachment content. If this is a URL to a folder, then for the folder to be displayed correctly in Outlook or Outlook on the web, set isFolder to true. Required.
        Args:
            value: Value to set for the sourceUrl property.
        """
        self._source_url = value
    
    @property
    def thumbnail_url(self,) -> Optional[str]:
        """
        Gets the thumbnailUrl property value. Applies to only a reference attachment of an image - URL to get a thumbnail image. Use thumbnailUrl and previewUrl only when sourceUrl identifies an image file. Optional.
        Returns: Optional[str]
        """
        return self._thumbnail_url
    
    @thumbnail_url.setter
    def thumbnail_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailUrl property value. Applies to only a reference attachment of an image - URL to get a thumbnail image. Use thumbnailUrl and previewUrl only when sourceUrl identifies an image file. Optional.
        Args:
            value: Value to set for the thumbnailUrl property.
        """
        self._thumbnail_url = value
    

