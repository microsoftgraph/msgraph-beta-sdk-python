from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ApplyPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the apply method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new applyPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The excludeGroups property
        self._exclude_groups: Optional[List[str]] = None
        # The includeAllUsers property
        self._include_all_users: Optional[bool] = None
        # The includeGroups property
        self._include_groups: Optional[List[str]] = None
        # The managementTemplateId property
        self._management_template_id: Optional[str] = None
        # The tenantGroupId property
        self._tenant_group_id: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplyPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplyPostRequestBody()
    
    @property
    def exclude_groups(self,) -> Optional[List[str]]:
        """
        Gets the excludeGroups property value. The excludeGroups property
        Returns: Optional[List[str]]
        """
        return self._exclude_groups
    
    @exclude_groups.setter
    def exclude_groups(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeGroups property value. The excludeGroups property
        Args:
            value: Value to set for the excludeGroups property.
        """
        self._exclude_groups = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exclude_groups": lambda n : setattr(self, 'exclude_groups', n.get_collection_of_primitive_values(str)),
            "include_all_users": lambda n : setattr(self, 'include_all_users', n.get_bool_value()),
            "include_groups": lambda n : setattr(self, 'include_groups', n.get_collection_of_primitive_values(str)),
            "management_template_id": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "tenant_group_id": lambda n : setattr(self, 'tenant_group_id', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        return fields
    
    @property
    def include_all_users(self,) -> Optional[bool]:
        """
        Gets the includeAllUsers property value. The includeAllUsers property
        Returns: Optional[bool]
        """
        return self._include_all_users
    
    @include_all_users.setter
    def include_all_users(self,value: Optional[bool] = None) -> None:
        """
        Sets the includeAllUsers property value. The includeAllUsers property
        Args:
            value: Value to set for the includeAllUsers property.
        """
        self._include_all_users = value
    
    @property
    def include_groups(self,) -> Optional[List[str]]:
        """
        Gets the includeGroups property value. The includeGroups property
        Returns: Optional[List[str]]
        """
        return self._include_groups
    
    @include_groups.setter
    def include_groups(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeGroups property value. The includeGroups property
        Args:
            value: Value to set for the includeGroups property.
        """
        self._include_groups = value
    
    @property
    def management_template_id(self,) -> Optional[str]:
        """
        Gets the managementTemplateId property value. The managementTemplateId property
        Returns: Optional[str]
        """
        return self._management_template_id
    
    @management_template_id.setter
    def management_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateId property value. The managementTemplateId property
        Args:
            value: Value to set for the managementTemplateId property.
        """
        self._management_template_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("excludeGroups", self.exclude_groups)
        writer.write_bool_value("includeAllUsers", self.include_all_users)
        writer.write_collection_of_primitive_values("includeGroups", self.include_groups)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_str_value("tenantGroupId", self.tenant_group_id)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_group_id(self,) -> Optional[str]:
        """
        Gets the tenantGroupId property value. The tenantGroupId property
        Returns: Optional[str]
        """
        return self._tenant_group_id
    
    @tenant_group_id.setter
    def tenant_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantGroupId property value. The tenantGroupId property
        Args:
            value: Value to set for the tenantGroupId property.
        """
        self._tenant_group_id = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

