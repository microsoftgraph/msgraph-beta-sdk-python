from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_change, compliance_change_rule, deployment_audience, deployment_settings
    from .. import entity

from .. import entity

class UpdatePolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new updatePolicy and sets the default values.
        """
        super().__init__()
        # Specifies the audience to target.
        self._audience: Optional[deployment_audience.DeploymentAudience] = None
        # Rules for governing the automatic creation of compliance changes.
        self._compliance_change_rules: Optional[List[compliance_change_rule.ComplianceChangeRule]] = None
        # Compliance changes like content approvals which result in the automatic creation of deployments using the audience and deploymentSettings of the policy.
        self._compliance_changes: Optional[List[compliance_change.ComplianceChange]] = None
        # The date and time when the update policy was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # Settings for governing how to deploy content.
        self._deployment_settings: Optional[deployment_settings.DeploymentSettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def audience(self,) -> Optional[deployment_audience.DeploymentAudience]:
        """
        Gets the audience property value. Specifies the audience to target.
        Returns: Optional[deployment_audience.DeploymentAudience]
        """
        return self._audience
    
    @audience.setter
    def audience(self,value: Optional[deployment_audience.DeploymentAudience] = None) -> None:
        """
        Sets the audience property value. Specifies the audience to target.
        Args:
            value: Value to set for the audience property.
        """
        self._audience = value
    
    @property
    def compliance_change_rules(self,) -> Optional[List[compliance_change_rule.ComplianceChangeRule]]:
        """
        Gets the complianceChangeRules property value. Rules for governing the automatic creation of compliance changes.
        Returns: Optional[List[compliance_change_rule.ComplianceChangeRule]]
        """
        return self._compliance_change_rules
    
    @compliance_change_rules.setter
    def compliance_change_rules(self,value: Optional[List[compliance_change_rule.ComplianceChangeRule]] = None) -> None:
        """
        Sets the complianceChangeRules property value. Rules for governing the automatic creation of compliance changes.
        Args:
            value: Value to set for the compliance_change_rules property.
        """
        self._compliance_change_rules = value
    
    @property
    def compliance_changes(self,) -> Optional[List[compliance_change.ComplianceChange]]:
        """
        Gets the complianceChanges property value. Compliance changes like content approvals which result in the automatic creation of deployments using the audience and deploymentSettings of the policy.
        Returns: Optional[List[compliance_change.ComplianceChange]]
        """
        return self._compliance_changes
    
    @compliance_changes.setter
    def compliance_changes(self,value: Optional[List[compliance_change.ComplianceChange]] = None) -> None:
        """
        Sets the complianceChanges property value. Compliance changes like content approvals which result in the automatic creation of deployments using the audience and deploymentSettings of the policy.
        Args:
            value: Value to set for the compliance_changes property.
        """
        self._compliance_changes = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the update policy was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the update policy was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
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
        Gets the deploymentSettings property value. Settings for governing how to deploy content.
        Returns: Optional[deployment_settings.DeploymentSettings]
        """
        return self._deployment_settings
    
    @deployment_settings.setter
    def deployment_settings(self,value: Optional[deployment_settings.DeploymentSettings] = None) -> None:
        """
        Sets the deploymentSettings property value. Settings for governing how to deploy content.
        Args:
            value: Value to set for the deployment_settings property.
        """
        self._deployment_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_change, compliance_change_rule, deployment_audience, deployment_settings
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
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
    

