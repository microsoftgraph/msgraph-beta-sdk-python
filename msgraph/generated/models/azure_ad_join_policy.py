from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_scope = lazy_import('msgraph.generated.models.policy_scope')

class AzureAdJoinPolicy(AdditionalDataHolder, Parsable):
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
    
    @property
    def allowed_groups(self,) -> Optional[List[str]]:
        """
        Gets the allowedGroups property value. The identifiers of the groups that are in the scope of the policy. Required when the appliesTo property is set to selected.
        Returns: Optional[List[str]]
        """
        return self._allowed_groups
    
    @allowed_groups.setter
    def allowed_groups(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedGroups property value. The identifiers of the groups that are in the scope of the policy. Required when the appliesTo property is set to selected.
        Args:
            value: Value to set for the allowedGroups property.
        """
        self._allowed_groups = value
    
    @property
    def allowed_users(self,) -> Optional[List[str]]:
        """
        Gets the allowedUsers property value. The identifiers of users that are in the scope of the policy. Required when the appliesTo property is set to selected.
        Returns: Optional[List[str]]
        """
        return self._allowed_users
    
    @allowed_users.setter
    def allowed_users(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedUsers property value. The identifiers of users that are in the scope of the policy. Required when the appliesTo property is set to selected.
        Args:
            value: Value to set for the allowedUsers property.
        """
        self._allowed_users = value
    
    @property
    def applies_to(self,) -> Optional[policy_scope.PolicyScope]:
        """
        Gets the appliesTo property value. Specifies whether to block or allow fine-grained control of the policy scope. The possible values are: 0 (meaning none), 1 (meaning all), 2 (meaning selected), 3 (meaning unknownFutureValue). The default value is 1. When set to 2, at least one user or group identifier must be specified in either allowedUsers or allowedGroups.  Setting this property to 0 or 1 removes all identifiers in both allowedUsers and allowedGroups.
        Returns: Optional[policy_scope.PolicyScope]
        """
        return self._applies_to
    
    @applies_to.setter
    def applies_to(self,value: Optional[policy_scope.PolicyScope] = None) -> None:
        """
        Sets the appliesTo property value. Specifies whether to block or allow fine-grained control of the policy scope. The possible values are: 0 (meaning none), 1 (meaning all), 2 (meaning selected), 3 (meaning unknownFutureValue). The default value is 1. When set to 2, at least one user or group identifier must be specified in either allowedUsers or allowedGroups.  Setting this property to 0 or 1 removes all identifiers in both allowedUsers and allowedGroups.
        Args:
            value: Value to set for the appliesTo property.
        """
        self._applies_to = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new azureAdJoinPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifiers of the groups that are in the scope of the policy. Required when the appliesTo property is set to selected.
        self._allowed_groups: Optional[List[str]] = None
        # The identifiers of users that are in the scope of the policy. Required when the appliesTo property is set to selected.
        self._allowed_users: Optional[List[str]] = None
        # Specifies whether to block or allow fine-grained control of the policy scope. The possible values are: 0 (meaning none), 1 (meaning all), 2 (meaning selected), 3 (meaning unknownFutureValue). The default value is 1. When set to 2, at least one user or group identifier must be specified in either allowedUsers or allowedGroups.  Setting this property to 0 or 1 removes all identifiers in both allowedUsers and allowedGroups.
        self._applies_to: Optional[policy_scope.PolicyScope] = None
        # Specifies whether this policy scope is configurable by the admin. The default value is false. When an admin has enabled Intune (MEM) to manage devices, this property is set to false and appliesTo defaults to 1 (meaning all).
        self._is_admin_configurable: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureAdJoinPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AzureAdJoinPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AzureAdJoinPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_groups": lambda n : setattr(self, 'allowed_groups', n.get_collection_of_primitive_values(str)),
            "allowed_users": lambda n : setattr(self, 'allowed_users', n.get_collection_of_primitive_values(str)),
            "applies_to": lambda n : setattr(self, 'applies_to', n.get_enum_value(policy_scope.PolicyScope)),
            "is_admin_configurable": lambda n : setattr(self, 'is_admin_configurable', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_admin_configurable(self,) -> Optional[bool]:
        """
        Gets the isAdminConfigurable property value. Specifies whether this policy scope is configurable by the admin. The default value is false. When an admin has enabled Intune (MEM) to manage devices, this property is set to false and appliesTo defaults to 1 (meaning all).
        Returns: Optional[bool]
        """
        return self._is_admin_configurable
    
    @is_admin_configurable.setter
    def is_admin_configurable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAdminConfigurable property value. Specifies whether this policy scope is configurable by the admin. The default value is false. When an admin has enabled Intune (MEM) to manage devices, this property is set to false and appliesTo defaults to 1 (meaning all).
        Args:
            value: Value to set for the isAdminConfigurable property.
        """
        self._is_admin_configurable = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("allowedGroups", self.allowed_groups)
        writer.write_collection_of_primitive_values("allowedUsers", self.allowed_users)
        writer.write_enum_value("appliesTo", self.applies_to)
        writer.write_bool_value("isAdminConfigurable", self.is_admin_configurable)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

