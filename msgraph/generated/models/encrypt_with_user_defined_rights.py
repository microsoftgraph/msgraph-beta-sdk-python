from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

encrypt_content = lazy_import('msgraph.generated.models.encrypt_content')

class EncryptWithUserDefinedRights(encrypt_content.EncryptContent):
    @property
    def allow_ad_hoc_permissions(self,) -> Optional[bool]:
        """
        Gets the allowAdHocPermissions property value. The allowAdHocPermissions property
        Returns: Optional[bool]
        """
        return self._allow_ad_hoc_permissions
    
    @allow_ad_hoc_permissions.setter
    def allow_ad_hoc_permissions(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAdHocPermissions property value. The allowAdHocPermissions property
        Args:
            value: Value to set for the allowAdHocPermissions property.
        """
        self._allow_ad_hoc_permissions = value
    
    @property
    def allow_mail_forwarding(self,) -> Optional[bool]:
        """
        Gets the allowMailForwarding property value. The allowMailForwarding property
        Returns: Optional[bool]
        """
        return self._allow_mail_forwarding
    
    @allow_mail_forwarding.setter
    def allow_mail_forwarding(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowMailForwarding property value. The allowMailForwarding property
        Args:
            value: Value to set for the allowMailForwarding property.
        """
        self._allow_mail_forwarding = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EncryptWithUserDefinedRights and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.encryptWithUserDefinedRights"
        # The allowAdHocPermissions property
        self._allow_ad_hoc_permissions: Optional[bool] = None
        # The allowMailForwarding property
        self._allow_mail_forwarding: Optional[bool] = None
        # The decryptionRightsManagementTemplateId property
        self._decryption_rights_management_template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EncryptWithUserDefinedRights:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EncryptWithUserDefinedRights
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EncryptWithUserDefinedRights()
    
    @property
    def decryption_rights_management_template_id(self,) -> Optional[str]:
        """
        Gets the decryptionRightsManagementTemplateId property value. The decryptionRightsManagementTemplateId property
        Returns: Optional[str]
        """
        return self._decryption_rights_management_template_id
    
    @decryption_rights_management_template_id.setter
    def decryption_rights_management_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the decryptionRightsManagementTemplateId property value. The decryptionRightsManagementTemplateId property
        Args:
            value: Value to set for the decryptionRightsManagementTemplateId property.
        """
        self._decryption_rights_management_template_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_ad_hoc_permissions": lambda n : setattr(self, 'allow_ad_hoc_permissions', n.get_bool_value()),
            "allow_mail_forwarding": lambda n : setattr(self, 'allow_mail_forwarding', n.get_bool_value()),
            "decryption_rights_management_template_id": lambda n : setattr(self, 'decryption_rights_management_template_id', n.get_str_value()),
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
        writer.write_bool_value("allowAdHocPermissions", self.allow_ad_hoc_permissions)
        writer.write_bool_value("allowMailForwarding", self.allow_mail_forwarding)
        writer.write_str_value("decryptionRightsManagementTemplateId", self.decryption_rights_management_template_id)
    

