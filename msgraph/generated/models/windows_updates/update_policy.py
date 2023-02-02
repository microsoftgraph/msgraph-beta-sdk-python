from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
compliance_change = lazy_import('msgraph.generated.models.windows_updates.compliance_change')
compliance_change_rule = lazy_import('msgraph.generated.models.windows_updates.compliance_change_rule')
deployment_audience = lazy_import('msgraph.generated.models.windows_updates.deployment_audience')
deployment_settings = lazy_import('msgraph.generated.models.windows_updates.deployment_settings')

class UpdatePolicy(entity.Entity):
    @property
    def audience(self,) -> Optional[deployment_audience.DeploymentAudience]:
        """
        Gets the audience property value. The audience property
        Returns: Optional[deployment_audience.DeploymentAudience]
        """
        return self._audience
    
    @audience.setter
    def audience(self,value: Optional[deployment_audience.DeploymentAudience] = None) -> None:
        """
        Sets the audience property value. The audience property
        Args:
            value: Value to set for the audience property.
        """
        self._audience = value
    
    @property
    def compliance_change_rules(self,) -> Optional[List[compliance_change_rule.ComplianceChangeRule]]:
        """
        Gets the complianceChangeRules property value. The complianceChangeRules property
        Returns: Optional[List[compliance_change_rule.ComplianceChangeRule]]
        """
        return self._compliance_change_rules
    
    @compliance_change_rules.setter
    def compliance_change_rules(self,value: Optional[List[compliance_change_rule.ComplianceChangeRule]] = None) -> None:
        """
        Sets the complianceChangeRules property value. The complianceChangeRules property
        Args:
            value: Value to set for the compliance_change_rules property.
        """
        self._compliance_change_rules = value
    
    @property
    def compliance_changes(self,) -> Optional[List[compliance_change.ComplianceChange]]:
        """
        Gets the complianceChanges property value. The complianceChanges property
        Returns: Optional[List[compliance_change.ComplianceChange]]
        """
        return self._compliance_changes
    
    @compliance_changes.setter
    def compliance_changes(self,value: Optional[List[compliance_change.ComplianceChange]] = None) -> None:
        """
        Sets the complianceChanges property value. The complianceChanges property
        Args:
            value: Value to set for the compliance_changes property.
        """
        self._compliance_changes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new updatePolicy and sets the default values.
        """
        super().__init__()
        # The audience property
        self._audience: Optional[deployment_audience.DeploymentAudience] = None
        # The complianceChangeRules property
        self._compliance_change_rules: Optional[List[compliance_change_rule.ComplianceChangeRule]] = None
        # The complianceChanges property
        self._compliance_changes: Optional[List[compliance_change.ComplianceChange]] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The deploymentSettings property
        self._deployment_settings: Optional[deployment_settings.DeploymentSettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdatePolicy()
    
    @property
    def deployment_settings(self,) -> Optional[deployment_settings.DeploymentSettings]:
        """
        Gets the deploymentSettings property value. The deploymentSettings property
        Returns: Optional[deployment_settings.DeploymentSettings]
        """
        return self._deployment_settings
    
    @deployment_settings.setter
    def deployment_settings(self,value: Optional[deployment_settings.DeploymentSettings] = None) -> None:
        """
        Sets the deploymentSettings property value. The deploymentSettings property
        Args:
            value: Value to set for the deployment_settings property.
        """
        self._deployment_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audience": lambda n : setattr(self, 'audience', n.get_object_value(deployment_audience.DeploymentAudience)),
            "complianceChanges": lambda n : setattr(self, 'compliance_changes', n.get_collection_of_object_values(compliance_change.ComplianceChange)),
            "complianceChangeRules": lambda n : setattr(self, 'compliance_change_rules', n.get_collection_of_object_values(compliance_change_rule.ComplianceChangeRule)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deploymentSettings": lambda n : setattr(self, 'deployment_settings', n.get_object_value(deployment_settings.DeploymentSettings)),
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
        writer.write_object_value("audience", self.audience)
        writer.write_collection_of_object_values("complianceChanges", self.compliance_changes)
        writer.write_collection_of_object_values("complianceChangeRules", self.compliance_change_rules)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("deploymentSettings", self.deployment_settings)
    

