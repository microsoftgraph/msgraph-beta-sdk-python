from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment = lazy_import('msgraph.generated.models.attachment')
extension = lazy_import('msgraph.generated.models.extension')
item_body = lazy_import('msgraph.generated.models.item_body')
multi_value_legacy_extended_property = lazy_import('msgraph.generated.models.multi_value_legacy_extended_property')
outlook_item = lazy_import('msgraph.generated.models.outlook_item')
single_value_legacy_extended_property = lazy_import('msgraph.generated.models.single_value_legacy_extended_property')

class Note(outlook_item.OutlookItem):
    @property
    def attachments(self,) -> Optional[List[attachment.Attachment]]:
        """
        Gets the attachments property value. The attachments property
        Returns: Optional[List[attachment.Attachment]]
        """
        return self._attachments
    
    @attachments.setter
    def attachments(self,value: Optional[List[attachment.Attachment]] = None) -> None:
        """
        Sets the attachments property value. The attachments property
        Args:
            value: Value to set for the attachments property.
        """
        self._attachments = value
    
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. The body property
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. The body property
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Note and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.note"
        # The attachments property
        self._attachments: Optional[List[attachment.Attachment]] = None
        # The body property
        self._body: Optional[item_body.ItemBody] = None
        # The extensions property
        self._extensions: Optional[List[extension.Extension]] = None
        # The hasAttachments property
        self._has_attachments: Optional[bool] = None
        # The isDeleted property
        self._is_deleted: Optional[bool] = None
        # The multiValueExtendedProperties property
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        # The singleValueExtendedProperties property
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
        # The subject property
        self._subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Note:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Note
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Note()
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The extensions property
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The extensions property
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(attachment.Attachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "is_deleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. The hasAttachments property
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. The hasAttachments property
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def is_deleted(self,) -> Optional[bool]:
        """
        Gets the isDeleted property value. The isDeleted property
        Returns: Optional[bool]
        """
        return self._is_deleted
    
    @is_deleted.setter
    def is_deleted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeleted property value. The isDeleted property
        Args:
            value: Value to set for the isDeleted property.
        """
        self._is_deleted = value
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The multiValueExtendedProperties property
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The multiValueExtendedProperties property
        Args:
            value: Value to set for the multiValueExtendedProperties property.
        """
        self._multi_value_extended_properties = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("body", self.body)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_str_value("subject", self.subject)
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The singleValueExtendedProperties property
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The singleValueExtendedProperties property
        Args:
            value: Value to set for the singleValueExtendedProperties property.
        """
        self._single_value_extended_properties = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

